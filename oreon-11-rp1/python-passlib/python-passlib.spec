%global source0_hash 7830b9323d9ba96a841ad698a8dec1d43a2b0b7f1c855c76772e7972c1c6d959
Name:           python-passlib
Version:        1.9.3
Release:        3%{?dist}
Summary:        Comprehensive password hashing framework supporting over 20 schemes
License:        BSD-3-Clause AND Beerware AND UnixCrypt AND ISC
URL:            https://github.com/notypecheck/passlib
Source0:        https://files.pythonhosted.org/packages/source/l/libpass/libpass-%{version}.tar.gz
Patch:          passlib-bcrypt5-truncate.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-passlib = %{version}-%{release}
# /oreon:deps
%package -n       python3-passlib+argon2
Summary:        Metapackage for python3-passlib argon2 extras
Requires:       python3-passlib = %{version}-%{release}
Requires:       python3dist(argon2-cffi) >= 18.2.0
Provides:       python3dist(passlib[argon2]) = %{version}-%{release}

%description -n python3-passlib+argon2
Metapackage for python3-passlib argon2 extras.

%package -n       python3-passlib+bcrypt
Summary:        Metapackage for python3-passlib bcrypt extras
Requires:       python3-passlib = %{version}-%{release}
Requires:       python3dist(bcrypt) >= 3.1.0
Provides:       python3dist(passlib[bcrypt]) = %{version}-%{release}

%description -n python3-passlib+bcrypt
Metapackage for python3-passlib bcrypt extras.

%package -n       python3-passlib+totp
Summary:        Metapackage for python3-passlib totp extras
Requires:       python3-passlib = %{version}-%{release}
Requires:       python3dist(cryptography) >= 43.0.1
Provides:       python3dist(passlib[totp]) = %{version}-%{release}

%description -n python3-passlib+totp
Metapackage for python3-passlib totp extras.

%description

%package -n python3-passlib
Summary:        Comprehensive password hashing framework supporting over 20 schemes
Provides:       python3dist(passlib) = %{version}
Provides:       python3dist(libpass) = %{version}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%description -n python3-passlib

# el9 missing argon2 https://bugzilla.redhat.com/show_bug.cgi?id=2089340

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libpass-%{version}
%oreon_prep
%build

%pyproject_wheel
%global legacy_distinfo passlib-%{version}.dist-info
mkdir %{legacy_distinfo}
cat > %{legacy_distinfo}/METADATA << EOF
Metadata-Version: 2.1
Name: passlib
Version: %{version}
EOF
echo rpm > %{legacy_distinfo}/INSTALLER
%install
%pyproject_install
cp -a %{legacy_distinfo} %{buildroot}%{python3_sitelib}
%oreon_autofiles python3-passlib usr/lib/python3*/site-packages/passlib* usr/lib64/python3*/site-packages/passlib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/passlib* usr/lib64/python3*/site-packages/passlib* usr/bin/*

%check

%pytest
%{py3_test_envvars} %{python3} -c 'import importlib.metadata as im; assert im.version("passlib") == im.version("libpass") == "%{version}"'
%files
%files -n python3-passlib -f %{oreon_filedir}/python3-passlib.list

%changelog

%autochangelog
