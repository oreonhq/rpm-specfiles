%global source0_hash 4064c590e59ce2e8d82a2f66d35f3120d765828b4df5e3dbfb07b4a8c24686c9
Name:           python-asyncssh
Version:        2.24.0
Release:        1%{?dist}
Summary:        AsyncSSH: Asynchronous SSHv2 client and server library
License:        EPL-2.0 OR GPL-2.0-or-later
URL:            http://asyncssh.timeheart.net
Source0:        https://files.pythonhosted.org/packages/source/a/asyncssh/asyncssh-%{version}.tar.gz
BuildArch:      noarch
Patch0:         libnacl-dep-cleanup.patch
Patch1:         aiofiles-context-manager.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-asyncssh = %{version}-%{release}
# /oreon:deps
%package -n       python3-asyncssh+bcrypt
Summary:        Metapackage for python3-asyncssh bcrypt extras
Requires:       python3-asyncssh = %{version}-%{release}
Requires:       python3dist(bcrypt) >= 3.1.3
Provides:       python3dist(asyncssh[bcrypt]) = %{version}-%{release}

%description -n python3-asyncssh+bcrypt
Metapackage for python3-asyncssh bcrypt extras.

%package -n       python3-asyncssh+fido2
Summary:        Metapackage for python3-asyncssh fido2 extras
Requires:       python3-asyncssh = %{version}-%{release}
Requires:       python3dist(fido2) >= 2
Provides:       python3dist(asyncssh[fido2]) = %{version}-%{release}

%description -n python3-asyncssh+fido2
Metapackage for python3-asyncssh fido2 extras.

%package -n       python3-asyncssh+ifaddr
Summary:        Metapackage for python3-asyncssh ifaddr extras
Requires:       python3-asyncssh = %{version}-%{release}
Requires:       python3dist(ifaddr) >= 0.2.0
Provides:       python3dist(asyncssh[ifaddr]) = %{version}-%{release}

%description -n python3-asyncssh+ifaddr
Metapackage for python3-asyncssh ifaddr extras.

%package -n       python3-asyncssh+gssapi
Summary:        Metapackage for python3-asyncssh gssapi extras
Requires:       python3-asyncssh = %{version}-%{release}
Requires:       python3dist(gssapi) >= 1.2.0
Provides:       python3dist(asyncssh[gssapi]) = %{version}-%{release}

%description -n python3-asyncssh+gssapi
Metapackage for python3-asyncssh gssapi extras.

%package -n       python3-asyncssh+pkcs11
Summary:        Metapackage for python3-asyncssh pkcs11 extras
Requires:       python3-asyncssh = %{version}-%{release}
Requires:       python3dist(python-pkcs11) >= 0.7.0
Provides:       python3dist(asyncssh[pkcs11]) = %{version}-%{release}

%description -n python3-asyncssh+pkcs11
Metapackage for python3-asyncssh pkcs11 extras.

%package -n       python3-asyncssh+pyOpenSSL
Summary:        Metapackage for python3-asyncssh pyOpenSSL extras
Requires:       python3-asyncssh = %{version}-%{release}
Requires:       python3dist(pyopenssl) >= 23.0.0
Provides:       python3dist(asyncssh[pyOpenSSL]) = %{version}-%{release}

%description -n python3-asyncssh+pyOpenSSL
Metapackage for python3-asyncssh pyOpenSSL extras.

%package -n       python3-asyncssh+pywin32
Summary:        Metapackage for python3-asyncssh pywin32 extras
Requires:       python3-asyncssh = %{version}-%{release}
Requires:       python3dist(pywin32) >= 227
Provides:       python3dist(asyncssh[pywin32]) = %{version}-%{release}

%description -n python3-asyncssh+pywin32
Metapackage for python3-asyncssh pywin32 extras.

%description

%package -n     python3-asyncssh
Summary:        AsyncSSH: Asynchronous SSHv2 client and server library
# oreon:reqs
Requires:       python3dist(cryptography) >= 48.0.1
Requires:       python3dist(typing-extensions) >= 4.0.0
# /oreon:reqs
%description -n python3-asyncssh

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir asyncssh-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-asyncssh usr/lib/python3*/site-packages/asyncssh* usr/lib64/python3*/site-packages/asyncssh* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/asyncssh* usr/lib64/python3*/site-packages/asyncssh* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-asyncssh -f %{oreon_filedir}/python3-asyncssh.list

%changelog

%autochangelog

