%global source0_hash 3ede206672ae6bc90ec07b702c79321783f4ad8e58c2eddbc5e505bbc218f0b9

Name:           pysvn
Version:        1.9.21
Release:        13%{?dist}
Summary:        Pythonic style bindings for Subversion
License:        Apache-1.1
URL:            https://pysvn.sourceforge.io/
Source0:        http://pysvn.barrys-emacs.org/source_kits/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  subversion
BuildRequires:  subversion-devel
BuildRequires:  krb5-devel
BuildRequires:  neon-devel
BuildRequires:  apr-devel
BuildRequires:  openssl-devel
BuildRequires:  glibc-langpack-en

# Replace the usage of locale.getdefaultlocale() for python 3.11 support
Patch0001: initlocale.patch

%global _description\
Pythonic style bindings for Subversion\

%description %_description

%package -n python3-pysvn
Summary: Pythonic style bindings for Subversion
%{?python_provide:%python_provide python3-pysvn}
BuildRequires:    python3-devel
BuildRequires:    python3-pycxx-devel >= 7.1.8

%description -n python3-pysvn %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

# Remove bundled libs
rm -rf Import

%build
pushd Source
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py configure \
    --enable-debug --verbose --fixed-module-name --norpath

echo "optflags %{optflags}"
%{__sed} -i -e 's@-Wall -fPIC -fexceptions -frtti@%{optflags} -fPIC -frtti@' Makefile
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m 755 %{buildroot}%{python3_sitearch}/%{name}
%{__install} -p -m 644 Source/pysvn/__init__.py %{buildroot}%{python3_sitearch}/%{name}
%{__install} -p -m 755 Source/pysvn/_pysvn.so %{buildroot}%{python3_sitearch}/%{name}

%check
pushd Tests
# the tests expect a valid answer from locale.getdefaultlocale()
# C.UTF-8 does not work. Use en_US.utf-8.
LC_ALL=en_US.UTF-8 %{__make} -j1
popd

%files -n python3-pysvn
%doc Docs/pysvn.html Docs/pysvn_prog_guide.html Docs/pysvn_prog_ref.html
%doc Docs/pysvn_prog_ref.js
%doc Examples
%license LICENSE.txt
%{python3_sitearch}/%{name}

%changelog
%autochangelog
