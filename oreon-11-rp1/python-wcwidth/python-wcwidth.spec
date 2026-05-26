%bcond tests 1

Name:           python-wcwidth
Version:        0.6.0
Release:        %autorelease
Summary:        Measures number of Terminal column cells of wide-character codes

# part of the code is under HPND-Markus-Kuhn
License:        MIT AND HPND-Markus-Kuhn
URL:            https://github.com/jquast/wcwidth
Source:         %{pypi_source wcwidth}
# oreon url source checksums begin
%global source0_sha256 cdc4e4262d6ef9a1a57e018384cbeb1208d8abbc64176027e2c2455c81313159
%global source0_file wcwidth-0.6.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch

%description
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%package -n     python3-wcwidth
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-wcwidth
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/wcwidth-0.6.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cdc4e4262d6ef9a1a57e018384cbeb1208d8abbc64176027e2c2455c81313159" || { echo "oreon: Source0 SHA256 mismatch for wcwidth-0.6.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n wcwidth-%{version}
# skip coverage checks
sed -i -e 's|--cov[^[:space:]]*||g' tox.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l wcwidth

%check
%pyproject_check_import
%if %{with tests}
%pytest -v
%endif

%files -n python3-wcwidth -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.0-1
- Prepare for Oreon 11 (RP1)
