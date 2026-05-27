%global source0_hash 991b3f971c65081c780fa15645a030bdf9e21ee8734b9f6010638b83bae1ff83

# Override versioning to sync with upstream
Epoch:    1
Version:  9.000
Release:  %autorelease
URL:      https://github.com/JulietaUla/Montserrat

%global         foundry         julietaula
%global         fontlicense     OFL-1.1
%global         fontlicenses    OFL.txt
%global         fontdocs        README.md AUTHORS.txt CONTRIBUTORS.txt DESCRIPTION.en_us.html
%global         fontdocsex      %{fontlicenses}

%global common_description %{expand:
A typeface inspired by signs around the Montserrat area \
of Buenos Aires, Argentina.}

%global fontfamily0       Montserrat
%global fontsummary0      Base version of the Montserrat area inspired typeface
%global fontpkgheader0    %{expand:
Obsoletes: julietaula-montserrat-fonts-common < %{version}-%{release}
}
%global fonts0            fonts/otf/Montserrat-*.otf
%global fontconfs0        %{SOURCE10}
%global fontdescription  %{expand:
%{common_description}

This package provides the base fonts.}

%global fontfamily1       Montserrat Alternates
%global fontsummary1      A Montserrat area inspired typeface family alternate version
%global fonts1            fonts-alternates/otf/MontserratAlternates-*.otf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

This package provides an alternate version of the fonts.}

%global fontfamily2       Montserrat Underline
%global fontsummary2      A Montserrat area inspired typeface family underline version
%global fonts2            fonts-underline/otf/MontserratUnderline-*.otf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This package provides an underline version of the fonts.}

Source0:        https://github.com/JulietaUla/Montserrat/archive/v9.000.tar.gz#/Montserrat-9.000.tar.gz
Source10: 61-%{fontpkgname0}.conf
Source11: 61-%{fontpkgname1}.conf
Source12: 61-%{fontpkgname2}.conf

%fontpkg -a

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n Montserrat-%{version}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.000-1
- Prepare for Oreon 11 (RP1)
