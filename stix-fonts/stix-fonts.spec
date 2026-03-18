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


Source0:  %{forgesource0}
Source10: 65-%{fontpkgname0}.xml

%fontpkg -a

%package doc
Summary:   Optional documentation files of %{source_name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{source_name}.

%prep
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
