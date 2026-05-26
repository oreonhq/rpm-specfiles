# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 b6979e8f128ed3fc4873c812c0d7e1722b3bb3f12c0c20a85c98f5f40427a89d
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary:	Macros to process XSL formatting objects
Name:		passivetex
Version:	1.25
Release:  42%{?dist}
License:	MIT
URL: https://github.com/sebastianrahtz/passivetex
Source0:	https://github.com/sebastianrahtz/passivetex/archive/master.zip
#Fix leader length.
Patch0:		passivetex-1.21-leader.patch
BuildArch:	noarch
Requires: tex(latex)
Requires(post): tex(latex)
Requires:	tex(xmltex.tex)
BuildRequires: tex(latex)

%description
PassiveTeX is a library of TeX macros which can be used to process an
XML document which results from an XSL transformation to formatting
objects.


%prep
%oreon_verify_sources
%setup -q -n %{name}-master
%patch -P0 -p1 -b .leader

%install
rm -rf $RPM_BUILD_ROOT
install -m 0755 -p -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex/passivetex
install -m 0644 -p *.sty *.xmt $RPM_BUILD_ROOT%{_datadir}/texmf/tex/xmltex/passivetex

%build

%post
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :
/usr/bin/env - PATH=$PATH:%{_bindir} fmtutil-sys --all > /dev/null 2>&1
exit 0

%postun
[ -x %{_bindir}/texconfig-sys ] && %{_bindir}/texconfig-sys rehash 2> /dev/null || :
%{_bindir}/env - PATH=$PATH:%{_bindir} fmtutil-sys --all > /dev/null 2>&1
exit 0

%triggerin -- tetex-latex
%{_bindir}/env - PATH=$PATH:%{_bindir} fmtutil-sys --all > /dev/null 2>&1
exit 0

%files
%doc README.passivetex LICENSE
%{_datadir}/texmf/tex/xmltex/passivetex

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.25-42
- Prepare for Oreon 11 (RP1)
