"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[991],{3905:(e,r,n)=>{n.d(r,{Zo:()=>m,kt:()=>h});var t=n(7294);function a(e,r,n){return r in e?Object.defineProperty(e,r,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[r]=n,e}function i(e,r){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var t=Object.getOwnPropertySymbols(e);r&&(t=t.filter((function(r){return Object.getOwnPropertyDescriptor(e,r).enumerable}))),n.push.apply(n,t)}return n}function o(e){for(var r=1;r<arguments.length;r++){var n=null!=arguments[r]?arguments[r]:{};r%2?i(Object(n),!0).forEach((function(r){a(e,r,n[r])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(r){Object.defineProperty(e,r,Object.getOwnPropertyDescriptor(n,r))}))}return e}function l(e,r){if(null==e)return{};var n,t,a=function(e,r){if(null==e)return{};var n,t,a={},i=Object.keys(e);for(t=0;t<i.length;t++)n=i[t],r.indexOf(n)>=0||(a[n]=e[n]);return a}(e,r);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(t=0;t<i.length;t++)n=i[t],r.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var p=t.createContext({}),c=function(e){var r=t.useContext(p),n=r;return e&&(n="function"==typeof e?e(r):o(o({},r),e)),n},m=function(e){var r=c(e.components);return t.createElement(p.Provider,{value:r},e.children)},u={inlineCode:"code",wrapper:function(e){var r=e.children;return t.createElement(t.Fragment,{},r)}},s=t.forwardRef((function(e,r){var n=e.components,a=e.mdxType,i=e.originalType,p=e.parentName,m=l(e,["components","mdxType","originalType","parentName"]),s=c(n),h=a,f=s["".concat(p,".").concat(h)]||s[h]||u[h]||i;return n?t.createElement(f,o(o({ref:r},m),{},{components:n})):t.createElement(f,o({ref:r},m))}));function h(e,r){var n=arguments,a=r&&r.mdxType;if("string"==typeof e||a){var i=n.length,o=new Array(i);o[0]=s;var l={};for(var p in r)hasOwnProperty.call(r,p)&&(l[p]=r[p]);l.originalType=e,l.mdxType="string"==typeof e?e:a,o[1]=l;for(var c=2;c<i;c++)o[c]=n[c];return t.createElement.apply(null,o)}return t.createElement.apply(null,n)}s.displayName="MDXCreateElement"},5972:(e,r,n)=>{n.r(r),n.d(r,{assets:()=>p,contentTitle:()=>o,default:()=>u,frontMatter:()=>i,metadata:()=>l,toc:()=>c});var t=n(7462),a=(n(7294),n(3905));const i={},o="02.09.2022 report",l={permalink:"/EF-Informatik/02.09.2022",editUrl:"https://github.com/GabrielMariethoz/EF-Informatik/tree/main/blog/02.09.2022.md",source:"@site/blog/02.09.2022.md",title:"02.09.2022 report",description:"Today we were programming with the help of lists. The exercices were easy except for the prime number exercice. I only didn't think long enough.",date:"2023-02-10T14:19:48.000Z",formattedDate:"10. Februar 2023",tags:[],readingTime:.985,hasTruncateMarker:!1,authors:[],frontMatter:{},nextItem:{title:"02.12.2022-arbeiten-an-numtrip",permalink:"/EF-Informatik/02.12.2022-arbeiten-an-numtrip"}},p={authorsImageUrls:[]},c=[{value:"Prime number exercice",id:"prime-number-exercice",level:3}],m={toc:c};function u(e){let{components:r,...i}=e;return(0,a.kt)("wrapper",(0,t.Z)({},m,i,{components:r,mdxType:"MDXLayout"}),(0,a.kt)("p",null,"Today we were programming with the help of lists. The exercices were easy except for the prime number exercice. I only didn't think long enough. "),(0,a.kt)("p",null,"The solution for the listen word riddle 2 exercice is:"),(0,a.kt)("p",null,(0,a.kt)("img",{src:n(8746).Z,width:"799",height:"729"})),(0,a.kt)("h3",{id:"prime-number-exercice"},"Prime number exercice"),(0,a.kt)("p",null,"The problem was that with the code below, the number is divided by another number and the rest isn't an integer once then it's an prime number. That's false! "),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-py"},"# !!! Code funktioniert nicht !!!\n\nzahlen = []\nprimzahlen = []\n\nfor counter in range(2, 101):\n    zahlen.append(counter)\n\nfor zahl in zahlen:\n    for primzahl in primzahlen:\n        if zahl % primzahl != 0:\n            primzahlen.append(zahl)\n\nprint(primzahlen)\n")),(0,a.kt)("p",null,"My solution was to create a boolean variable that is initiated as true. If the number divided by the prime number has no rest once, the bool is set to false. After the number was divided by all prime numbers the code checks if the bool is still true."),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-py"},"zahlen = []\nprimzahlen = []\nprimzahl_bool = True\n\nfor counter in range(2, 101):\n    zahlen.append(counter)\n\n\nfor zahl in zahlen:\n    for primzahl in primzahlen:\n        if zahl % primzahl == 0:\n            primzahl_bool = False\n\n    if primzahl_bool == True:\n        primzahlen.append(zahl)\n    primzahl_bool = True\n\nprint(primzahlen)\n\n")))}u.isMDXComponent=!0},8746:(e,r,n)=>{n.d(r,{Z:()=>t});const t=n.p+"assets/images/r_1798534_nBE8D-c6db7ee3ff104f3478b44565446cfde4.jpg"}}]);