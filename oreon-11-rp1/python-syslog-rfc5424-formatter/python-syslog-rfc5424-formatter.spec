%global source0_hash 9bc5c9c3fb6a92b6f85ca108f2be04ea50106113324b5d7b1f07fcc6ad2766d3

%global pypi_name syslog-rfc5424-formatter

Name:           python-%{pypi_name}
Version:        1.2.3
Release:        15%{?dist}
Summary:        Logging formatter which produces well-formatted RFC5424 Syslog Protocol messages

License:        ISC
URL:            https://github.com/easypost/syslog-rfc5424-formatter
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
This module implements a python logging formatter which produces well-formed
RFC5424-compatible Syslog messages to a given socket.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This module implements a python logging formatter which produces well-formed
RFC5424-compatible Syslog messages to a given socket.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files syslog_rfc5424_formatter

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md
%doc CHANGES.md

%changelog
%autochangelog
