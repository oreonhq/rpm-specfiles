%global source0_hash 4abc6d7097b2e0ad83b57a5f047256870aebe6c8e0af4b85c2d839e257f35810

Name:           sasutils
Version:        0.6.1
Release:        8%{?dist}
Summary:        Serial Attached SCSI (SAS) utilities
License:        Apache-2.0
URL:            https://github.com/stanford-rc/sasutils
Source0:        https://files.pythonhosted.org/packages/source/s/sasutils/sasutils-%{version}.tar.gz#/sasutils-%{version}.pypi.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       sg3_utils
Requires:       smp_utils

%description
sasutils is a set of command-line tools and a Python library to ease the
administration of Serial Attached SCSI (SAS) fabrics.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n sasutils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sasutils

# Man pages
install -d %{buildroot}%{_mandir}/man1
install -p -m 0644 doc/man/man1/sas_counters.1 %{buildroot}%{_mandir}/man1/
install -p -m 0644 doc/man/man1/sas_devices.1 %{buildroot}%{_mandir}/man1/
install -p -m 0644 doc/man/man1/sas_discover.1 %{buildroot}%{_mandir}/man1/
install -p -m 0644 doc/man/man1/ses_report.1 %{buildroot}%{_mandir}/man1/

%check
# No test suite yet

%files -f %{pyproject_files}
%{_bindir}/sas_counters
%{_bindir}/sas_devices
%{_bindir}/sas_discover
%{_bindir}/sas_mpath_snic_alias
%{_bindir}/sas_sd_snic_alias
%{_bindir}/sas_st_snic_alias
%{_bindir}/ses_report
%{_mandir}/man1/sas_counters.1*
%{_mandir}/man1/sas_devices.1*
%{_mandir}/man1/sas_discover.1*
%{_mandir}/man1/ses_report.1*
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
