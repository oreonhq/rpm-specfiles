%global source0_hash 4509dc1fc8b34595fdb5f39b8a628c714af4d6d72eb4a7ca0c726c3e5d944173
%global pkgname django-reversion
Name:           python-django-reversion
Version:        6.3.0
Release:        1%{?dist}
Summary:        Version control extension for the Django web framework
License:        LicenseRef-Callaway-BSD
URL:            http://github.com/etianen/django-reversion
Source0:        https://github.com/etianen/django-reversion/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Provides:       %{pkgname} = %{version}-%{release}
Obsoletes:      %{pkgname} < 1.6.2-1
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

Features:
* Roll back to any point in a model's history - an unlimited undo facility!
* Recover deleted models - never lose data again!
* Admin integration for maximum usability.
* Group related changes into revisions that can be rolled back in a single
  transaction.
* Automatically save a new version whenever your model changes using Django's
  flexible signalling framework.
* Automate your revision management with easy-to-use middleware.

Reversion can be easily added to your existing Django project with a minimum
of code changes.

%package -n python3-%{pkgname}
Summary:        Version control extension for the Django web framework
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-django
%{?python_provide:%python_provide python3-%{pkgname}}
Obsoletes:   python-%{pkgname} < 2.0.13-1
Obsoletes:   python2-%{pkgname} < 2.0.13-1
%description -n python3-%{pkgname}
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities.

Features:
* Roll back to any point in a model's history - an unlimited undo facility!
* Recover deleted models - never lose data again!
* Admin integration for maximum usability.
* Group related changes into revisions that can be rolled back in a single
  transaction.
* Automatically save a new version whenever your model changes using Django's
  flexible signalling framework.
* Automate your revision management with easy-to-use middleware.

Reversion can be easily added to your existing Django project with a minimum
of code changes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version}

%build

%py3_build
%install
%py3_install
(cd $RPM_BUILD_ROOT && find . -name 'django*.mo') | %{__sed} -e 's|^.||' | %{__sed} -e \
  's:\(.*/locale/\)\([^/_]\+\)\(.*\.mo$\):%lang(\2) \1\2\3:' \
  >> %{name}.lang
find $RPM_BUILD_ROOT -name "*.po" | xargs rm -f
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-django-reversion -f %{oreon_filedir}/python3-django-reversion.list

%changelog

%autochangelog
