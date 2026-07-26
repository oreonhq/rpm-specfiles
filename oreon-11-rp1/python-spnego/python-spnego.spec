%global source0_hash 994388d308fb06e4498365ce78d222bf4f3570b6df4ec95738431f61510c971b

Name:           python-spnego
Version:        0.11.2
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
