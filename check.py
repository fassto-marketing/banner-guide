# 배너 가이드 푸시 전 정합성 검사 — python check.py (0건이어야 푸시)
# ponytail: 텍스트 패턴 검사만. 렌더 검증(SVG 잘림)은 브라우저에서 별도.
import io, re, sys
s = io.open("index.html", encoding="utf-8").read()
rules = {
    "줄표(—) 금지": s.count("—"),
    "질문형(~는가) 금지": len(re.findall(r"[가-힣]+는가", s)),
    "'두 벌' 금지(→2종)": s.count("두 벌"),
    "'등록' 금지(→전달/게시/지정)": s.count("등록"),
    "'셀러' 금지(FMS=물류 관리 시스템)": s.count("셀러"),
    "단정체(~이다.) 금지": len(re.findall(r"[가-힣]+이다\.", s)),
    "약자 물결(~Npx) 금지(→약 Npx)": len(re.findall(r"[^0-9]~\d+px", s)),
}
fail = {k: v for k, v in rules.items() if v}
for k, v in rules.items():
    print(("FAIL" if v else "ok  "), k, f"{v}건")
sys.exit(1 if fail else 0)
