%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name:       hunspell-tr
Summary:    Turkish hunspell dictionaries
Version:    1.1.0
License:    MIT
Release:    11%{?dist}

URL:        https://github.com/tdd-ai/hunspell-tr
Source:     https://github.com/tdd-ai/hunspell-tr/archive/v%{version}/%{name}-v%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 59948c131b98200f7b8221f4735b19ae77f5e842d3d2dbc7a6aa5b7e5f7aeef8
%global source0_file hunspell-tr-v1.1.0.tar.gz
# oreon url source checksums end


BuildArch:  noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-tr)

%description
Turkish hunspell dictionaries.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/hunspell-tr-v1.1.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "59948c131b98200f7b8221f4735b19ae77f5e842d3d2dbc7a6aa5b7e5f7aeef8" || { echo "oreon: Source0 SHA256 mismatch for hunspell-tr-v1.1.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
rm trspell10.csv

%build
# nothing to see here

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}


%files
%doc README.md
%license LICENSE
%{_datadir}/%{dict_dirname}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-11
- Prepare for Oreon 11 (RP1)
