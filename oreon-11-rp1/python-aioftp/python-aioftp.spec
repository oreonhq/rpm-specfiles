%global source0_hash 311f66e9ff726055f73e74764fb62e097ab806da3177c13f1356c8e7eaf9a65d
Name:           python-aioftp
Version:        0.28.0
Release:        1%{?dist}
Summary:        ftp client/server for asyncio
License:        ...
URL:            https://github.com/aio-libs/aioftp
Source0:        https://files.pythonhosted.org/packages/source/a/aioftp/aioftp-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aioftp = %{version}-%{release}
# /oreon:deps
%package -n       python3-aioftp+socks
Summary:        Metapackage for python3-aioftp socks extras
Requires:       python3-aioftp = %{version}-%{release}
Requires:       python3dist(siosocks) >= 0.2.0
Provides:       python3dist(aioftp[socks]) = %{version}-%{release}

%description -n python3-aioftp+socks
Metapackage for python3-aioftp socks extras.

%package -n       python3-aioftp+dev
Summary:        Metapackage for python3-aioftp dev extras
Requires:       python3-aioftp = %{version}-%{release}
Requires:       python3dist(async-timeout) >= 4.0.0
Provides:       python3dist(aioftp[dev]) = %{version}-%{release}

%description -n python3-aioftp+dev
Metapackage for python3-aioftp dev extras.

%description

%package -n     python3-aioftp
Summary:        ftp client/server for asyncio
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.13.2
# /oreon:reqs
%description -n python3-aioftp

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir aioftp-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aioftp usr/lib/python3*/site-packages/aioftp* usr/lib64/python3*/site-packages/aioftp* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aioftp* usr/lib64/python3*/site-packages/aioftp* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aioftp -f %{oreon_filedir}/python3-aioftp.list

%changelog

%autochangelog
