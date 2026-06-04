%global source0_hash 1e76b9ab0bb08372ff73ad5b58d9116260e9058d1fce4b83fe1e213c3b9c947f

# SPDX-License-Identifier: MIT
%global forgeurl https://github.com/stipub/stixfonts/
Version: 2.13b171
%forgemeta

Release: 10%{?dist}
URL:     http://www.stixfonts.org/

%global foundry           STIX
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          README.md FONTLOG.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        STIX
%global fontsummary       STIX, a scientific and engineering font family
%global fontpkgheader     %{expand:
Obsoletes: stix-math-fonts < %{version}-%{release}
}
%global fonts             fonts/static_otf/STIXTwoText*otf fonts/static_otf/STIXTwoMath*otf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
The mission of the Scientific and Technical Information Exchange (STIX) font
creation project is the preparation of a comprehensive set of fonts that serve
the scientific and engineering community in the process from manuscript
creation through final publication, both in electronic and print formats.
}


Source0:        https://github.com/stipub/stixfonts/archive/refs/tags/v2.13b171.tar.gz#/stixfonts-2.13b171.tar.gz
Source10: 65-%{fontpkgname0}.xml

%fontpkg -a

%package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%forgesetup

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%files doc
%doc docs/*pdf docs/*xlsx

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.13b171-10
- Prepare for Oreon 11 (RP1)
