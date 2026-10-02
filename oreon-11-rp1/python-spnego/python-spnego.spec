%global source0_hash 448a491a9bf0e5fb957567fe46e6809fa836aa40dfcccebcc740bb64acb1be1c

Name:           python-spnego
Version:        0.12.2
Release:        %autorelease
Summary:        Windows Negotiate Authentication Client and Server
# SPDX License
License:        MIT
URL:            https://github.com/jborean93/pyspnego
Source:         %{pypi_source pyspnego}
BuildArch:      noarch

%global _description %{expand:
Python SPNEGO Library to handle SPNEGO (Negotiate, NTLM, Kerberos)
authentication. Also includes a packet parser that can be used to
decode raw NTLM/SPNEGO/Kerberos tokens into a human readable format.}

%description %{_description}

%package -n     python3-spnego
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock

%description -n python3-spnego %{_description}

%pyproject_extras_subpkg -n python3-spnego kerberos

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pyspnego-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spnego

%check
%pytest -v tests

%files -n python3-spnego -f %{pyproject_files}
%doc README.md
%{_bindir}/pyspnego-parse

%changelog
%autochangelog
