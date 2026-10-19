%global source0_hash 6c52288dab069257cc831846d15d48133522455d4677ee69a9781f11dbefd815
Name:           python-userpath
Version:        1.9.2
Release:        1%{?dist}
Summary:        Cross-platform tool for adding locations to the user PATH
License:        MIT
URL:            https://github.com/ofek/userpath
Source0:        https://files.pythonhosted.org/packages/source/u/userpath/userpath-%{version}.tar.gz
Source10:       userpath.1
Source11:       userpath-append.1
Source12:       userpath-prepend.1
Source13:       userpath-verify.1
BuildArch:      noarch
%global common_description %{expand:
Cross-platform tool for adding locations to the user PATH, no elevated
privileges required!}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-userpath = %{version}-%{release}
# /oreon:deps
%description %common_description

%package -n     python3-userpath
Summary:        Cross-platform tool for adding locations to the user PATH
%description -n python3-userpath %common_description

%prep

%autosetup -p1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r '/^(coverage)$/d' requirements-dev.txt |
  tee requirements-dev.filtered.txt

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'
%oreon_autofiles python3-userpath usr/lib/python3*/site-packages/userpath* usr/lib64/python3*/site-packages/userpath* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/userpath* usr/lib64/python3*/site-packages/userpath* usr/bin/*

%build

%pyproject_wheel
%check

%pytest
%files
%files -n python3-userpath -f %{oreon_filedir}/python3-userpath.list

%changelog

%autochangelog
