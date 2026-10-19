%global source0_hash fc2c2ff4f03bf1a110f6ba2cadb874f51a7c0ce4fa0261d2bbe3371548ddbc88
Name:           python-systemd
Version:        236
Release:        1%{?dist}
Summary:        Python module wrapping libsystemd functionality
License:        LGPL-2.1-or-later
URL:            https://github.com/systemd/python-systemd
Source0:        https://github.com/systemd/python-systemd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  jq
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  systemd-devel
BuildRequires:  web-assets-devel
# /oreon:deps
%description

%package -n python3-systemd
Summary:        Python module wrapping libsystemd functionality
%{?python_provide:%python_provide python3-systemd}
Provides:       systemd-python3 = %{version}-%{release}
Provides:       systemd-python3%{?_isa} = %{version}-%{release}
Obsoletes:      systemd-python3 < 230
%description -n python3-systemd

%package doc
Summary:        HTML documentation for %{name}
Requires:       js-jquery
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
sed -i 's/py\.test/pytest/' Makefile

%build

make PYTHON=%{__python3} build
make PYTHON=%{__python3} SPHINX_BUILD=sphinx-build-3 sphinx-html
rm -r build/html/.buildinfo build/html/.doctrees
%install
%make_install PYTHON=%{__python3}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -rv build/html %{buildroot}%{_pkgdocdir}/
ln -vsf %{_jsdir}/jquery/latest/jquery.min.js %{buildroot}%{_pkgdocdir}/html/_static/jquery.js
cp -p README.md NEWS %{buildroot}%{_pkgdocdir}/
%oreon_autofiles python3-systemd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

test -f /run/systemd/journal/stdout || \
     sed -i 's/--doctest[^ ]*//g' pytest.ini
make PYTHON=%{__python3} check
%files -f %{oreon_filedir}/main.list
%files -n python3-systemd -f %{oreon_filedir}/python3-systemd.list
%files -n python-systemd-doc -f %{oreon_filedir}/python-systemd-doc.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 235-1
- Import
