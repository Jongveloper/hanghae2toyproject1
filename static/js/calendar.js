let date = new Date();

const renderCalendar = () => {
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();

    // querySelector 를 통해서 year-month 태그에 접근해서, 여기에 맞는 연도와 월을 넣어주기
    document.querySelector('.year-month').textContent = `${viewYear}년 ${viewMonth + 1}월`;

    // 1. 지난 달 마지막 날짜와 요일   2. 이번 달 마지막 날짜와 요일
    // 1번 정보를 통해서 지난 달 날짜 며칠을 몇 개를 그려내야 될지 결정   2번 정보를 통해서 다음 달 날짜 며칠, 몇 개를 그려내야 될지를 결정
    // 새로운 Date 객체를 생성할 때, 파라미터 date 에 해당하는 부분에 0을 전달하게 되면, 지난달의 마지막 날의 Date 객체가 생성된다
    // 같은 원리로 파라미터 다음 달의 0번째 날을 뽑으면, 이번 달의 마지막 날 Date 객체가 생성
    const prevLast = new Date(viewYear, viewMonth, 0);
    const thisLast = new Date(viewYear, viewMonth + 1, 0);

    const PLDate = prevLast.getDate();
    const PLDay = prevLast.getDay();

    const TLDate = thisLast.getDate();
    const TLDay = thisLast.getDay();

    // Dates 기본 배열들
    const prevDates = [];
    const thisDates = [...Array(TLDate + 1).keys()].slice(1);
    const nextDates = [];
    // 1. Array(n)으로 배열을 만들면 길이가 n인 배열이 생성된다 (이때 모든 요소들은 undefined)
    // 2. 그런데 모든 요소들이 empty 값이기 때문에 keys() 메서드를 활용하면 0부터 n - 1까지의 Array Iterator 가 생성되는데,
    // 3. 전개 구문을 통해서 이 Array Iterator 를 배열로 만들어 내면 0부터 n-1까지의 배열을 얻어낼 수가 있다
    // 4. 그래서 이번 달 마지막 날짜 + 1을 n에 전달해주고
    // 5. 제일 앞에 있는 0을 없애기 위해서 slice 메서드를 활용

    // 이전 달을 표현할 날짜들을 생성
    if (PLDay !== 6) {
        for (let i = 0; i < PLDay + 1; i++) {
            prevDates.unshift(PLDate - i);
        }
    }

    // 다음 달을 표현할 날짜
    for (let i = 1; i < 7 - TLDay; i++) {
        nextDates.push(i);
    }

    // concat 메서드를 통해서 세 배열을 합친 다음에, forEach 메서드로 전체 요소들을 돌면서, html 코드로 데이터를 하나씩 수정
    // Dates 합치기
    const dates = prevDates.concat(thisDates, nextDates);
    // Dates 정리
    const firstDateIndex = dates.indexOf(1);
    const lastDateIndex = dates.lastIndexOf(TLDate);

    // dates 배열을 모두 만들고서 forEach 로 HTML 을 만드는 부분
    // 지난달 부분을 알아내기 위해서 첫날의 index(firstDateIndex)를 찾았고
    // 다음 달 부분을 알아내기 위해서 마지막 날의 index(lastDateIndex)를 찾아줌
    // 그러고 나서 삼항 연산자를 통해서 이번 달에 해당하는 부분은 this, 그리고 나머지는 other 라는 문자열로 구분해서
    // 날짜 부분을 span 태그로 감싸서 class 로 지정
    // 이렇게 한 이유는, date 에 class 를 줄 경우에 투명도를 조절하게 되면,
    // 달력의 격자를 그리고 있는 테두리 부분도 같이 투명도가 같이 조절이 되기 때문에 글자만 투명도를 주기 위함
    dates.forEach((date, i) => {
        const condition = i >= firstDateIndex && i < lastDateIndex + 1
            ? 'this'
            : 'other';

        dates[i] = `<div class="date"><span class="${condition}">${date}</span></div>`;
    })

    // Dates 그리기
    document.querySelector('.dates').innerHTML = dates.join('');

    // 1. new Date()를 통해 오늘 날짜에 맞는 date 객체를 새로 만들어주고,
    // 2. viewMonth 와 viewYear 가 today 의 데이터와 같은지 비교를 한 다음
    // 3. 만약 2번이 충족된다면 this 라는 클래스를 가진 태그들을 모두 찾아내서 반복문을 돌려준다
    // 4. 그러고 나서 해당 태그가 가지고 있는 날짜는 문자열이기 때문에 + 단항 연산자를 통해 숫자로 변경한 뒤, 오늘 날짜와 비교하고
    // 5. 4번이 충족된다면 해당 태그에 today 라는 클래스를 추가하고 break 로 반복문을 종료해 주는 코드
    // 5번에서 break 를 하는 이유는 오늘 날짜는 하나밖에 없기 때문에 찾으면 더 이상 뒤의 반복을 할 필요가 없기 때문
    const today = new Date();
    if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
        for (let date of document.querySelectorAll('.this')) {
            if (+date.innerText === today.getDate()) {
                date.classList.add('today');
                break;
            }
        }
    }
};

renderCalendar();

// 지난 달
const prevMonth = () => {
    date.setMonth(date.getMonth() - 1);
    renderCalendar();
}
// 다음 달
const nextMonth = () => {
    date.setMonth(date.getMonth() + 1);
    renderCalendar();
}
// 오늘
const goToday = () => {
    date = new Date();
    renderCalendar();
}
// addEventListener 를 달아도 되긴 하지만 그냥 간단하게 HTML 태그에 onclick 속성으로 추가