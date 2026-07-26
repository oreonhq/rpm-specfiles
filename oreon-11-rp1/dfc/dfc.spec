%global source0_hash cea18fab1f053eddc359530816712edd1f497c556035a7c4d63ac87a4abc4b28

Name:           dfc
Version:        3.1.1
Release:        10%{?dist}
Summary:        Report file system space usage information with style

License:        BSD-3-Clause AND BSD-2-Clause
# main package cites BSD-3-Clause.
# cmake/modules/GettextTranslate.cmake specifically cites BSD-2-Clause
URL:            https://github.com/rolinh/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gettext

%description
dfc is a tool to report file system space usage information. When the
output is a terminal, it uses color and graphs by default. It has a lot of
features such as HTML, JSON and CSV export, multiple filtering options,
the ability to show mount options and so on.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake \
  -D SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install

rm -f %{buildroot}%{_docdir}/%{name}/{HACKING.md,LICENSE}

%find_lang %{name}
%find_lang %{name} --with-man

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS.md CHANGELOG.md README.md TRANSLATORS.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/xdg/%{name}/

%changelog
%autochangelog
