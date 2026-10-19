%global source0_hash a97d5549e9ad81fe17159ed02c68774ad5d266c72f8d9a0b5a9c371fe85d902b
Name:           python3-docs
Summary:        Documentation for the Python 3 programming language
%global         pybasever 3.14
%global         general_version %{pybasever}.3
%global         upstream_version %{general_version}%{?prerel}
Version:        %{general_version}%{?prerel:~%{prerel}}
Release:        1%{?dist}
License:        Python-2.0.1 AND (Python-2.0.1 OR 0BSD)
URL:            https://www.python.org/
Source0:        https://www.python.org/ftp/python/%{general_version}/Python-%{general_version}.tar.xz
BuildArch:      noarch
Recommends:     python3 = %{version}
%bcond_without linkchecker
%if %{with linkchecker}
%endif
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  linkchecker
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-docs-theme
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  python3-sphinx
# /oreon:deps
%description
The python3-docs package contains documentation on the Python 3
programming language and interpreter.

%prep

%autosetup -p1 -n Python-%{upstream_version}

%build

make -C Doc html PYTHON=%{__python3}
rm Doc/build/html/.buildinfo
%install
mkdir -p %{buildroot}
%oreon_autofiles main

%check

%if %{with linkchecker}
linkchecker \
  --ignore-url=^mailto: --ignore-url=^http --ignore-url=^ftp \
  --ignore-url=.txt\$ --no-warnings \
  Doc/build/html/index.html
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
