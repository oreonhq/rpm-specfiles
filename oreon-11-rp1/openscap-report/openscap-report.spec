%global pymodule_name openscap_report

Name:           openscap-report
Version:        1.0.0
Release:        7%{?dist}
Summary:        A tool for generating human-readable reports from (SCAP) XCCDF and ARF results

# The entire source code is LGPL-2.1+ and GPL-2.0+ and MIT except schemas/ and assets/, which are Public Domain
License:        LGPLv2+ and GPLv2+ and MIT and Public Domain
URL:            https://github.com/OpenSCAP/%{name}
Source0:        https://github.com/OpenSCAP/%{name}/releases/download/v%{version}/%{pymodule_name}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 ecdd455bb933a65076e9da9161b510c1dccbe2c452aa43efb117694c968d8763
%global source0_file openscap_report-1.0.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

Provides:       bundled(patternfly) = 4

Requires:       python3-lxml
Recommends:     redhat-display-fonts
Recommends:     redhat-text-fonts

Obsoletes:      oval-graph

%global _description %{expand:
This package provides a command-line tool for generating
human-readable reports from SCAP XCCDF and ARF results.}

%description %_description


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/openscap_report-1.0.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ecdd455bb933a65076e9da9161b510c1dccbe2c452aa43efb117694c968d8763" || { echo "oreon: Source0 SHA256 mismatch for openscap_report-1.0.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{pymodule_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires
# test requirement listed only in tox.ini
echo "%{py3_dist jsonschema}"


%build
%pyproject_wheel
sphinx-build -b man docs _build_docs



%install
%pyproject_install
%pyproject_save_files %{pymodule_name}
install -m 0644 -Dt %{buildroot}%{_mandir}/man1 _build_docs/oscap-report.1


%check
# test_store_file fails with FileNotFoundError: [Errno 2] No such file or directory: '/tmp/oscap-report-tests_result.html'
%pytest -k "not test_store_file"

%files -f %{pyproject_files}
%{_mandir}/man1/oscap-report.*
%{_bindir}/oscap-report
%exclude %{python3_sitelib}/tests/
%license LICENSE


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.0-7
- Import
