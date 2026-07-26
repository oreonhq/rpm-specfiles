%global source0_hash f039b7dd4746df56f6102097b3dc250fe0078be75130b9dc4211a85a3b1ec6a4

%global srcname kerberos
%global sum A high-level wrapper for Kerberos (GSSAPI) operations

Name:           python-%{srcname}
Version:        1.3.0
Release:        31%{?dist}
Summary:        %{sum}

License:        Apache-2.0
# SVN browser is at https://trac.calendarserver.org/browser/PyKerberos
URL:            https://pypi.python.org/pypi/kerberos
Source0:        https://pypi.python.org/packages/source/k/%{srcname}/%{srcname}-%{version}.tar.gz
Source1:        LICENSE

# SystemError thrown with Python 3.10
# https://github.com/apple/ccs-pykerberos/issues/88
# https://bugzilla.redhat.com/2008899
Patch1:         PY_SSIZE_T_CLEAN.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2245868
Patch2:         include_unistd.patch

BuildRequires:  python3-devel
BuildRequires:  python3-requests
BuildRequires:  krb5-devel
BuildRequires:  gcc

%global desc This Python package is a high-level wrapper for Kerberos (GSSAPI) operations.\
The goal is to avoid having to build a module that wraps the entire\
Kerberos framework, and instead offer a limited set of functions that do what\
is needed for client/server Kerberos authentication based on\
<http://www.ietf.org/rfc/rfc4559.txt>.

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
install -m 644 $RPM_SOURCE_DIR/LICENSE LICENSE 
%{pyproject_install}
%pyproject_save_files -L '*'

%check
%pyproject_check_import

# Regression test for https://bugzilla.redhat.com/2008899
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%{python3} -c 'import kerberos; kerberos.channelBindings(application_data=b"")'

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
