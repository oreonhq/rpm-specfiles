%global source0_hash db04a5920d25744edaf0705c8a85ac6d6291c9b33c999233fda314e0dad55cf3
%bcond pathops 0
%bcond autohint 1
%bcond json 1
%bcond repacker 1
Name:           fontmake
Version:        3.12.1
Release:        1%{?dist}
Summary:        Compile fonts from sources (UFO, Glyphs) to binary (OpenType, TrueType)
License:        Apache-2.0
SourceLicense:  %{license} AND MIT AND OFL-1.1
URL:            https://github.com/googlefonts/fontmake
Source0:        https://files.pythonhosted.org/packages/source/f/fontmake/fontmake-%{version}.tar.gz
BuildArch:      noarch
%py_provides python3-fontmake
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-fontmake = %{version}-%{release}
# /oreon:deps
%description
fontmake compiles fonts from various sources (.glyphs, .ufo, designspace) into
binaries (.otf, .ttf). You can use it to create static instances and variable
fonts.

%if %{with pathops}
%endif
%if %{with autohint}
%endif
%if %{with json}
%endif
%if %{with repacker}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
install -d '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man \
    --no-info \
    --name '%{summary}' \
    --output='%{buildroot}%{_mandir}/man1/fontmake.1' \
    %{buildroot}%{_bindir}/fontmake
%oreon_autofiles main

%check

%pyproject_check_import
k="${k-}${k+ and }not test_main_designspace_v5_builds_STAT"
%if %{without autohint}
k="${k-}${k+ and }not test_autohinting"
%endif
k="${k-}${k+ and }not test_data_independence"
k="${k-}${k+ and }not test_skipped_fontinfo_attributes"
%pytest -k "${k-}" -rs -vv
%files

%changelog

%autochangelog
