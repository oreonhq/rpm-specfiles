%global source0_hash 61d73c61f670d68ffc346829d24b2f1d2050aa561aa71cb98e2fb43992c27304

Name:           trac
Version:        1.6
Release:        11%{?dist}
Summary:        Enhanced wiki and issue tracking system
License:        BSD-3-Clause
URL:            http://trac.edgewall.com/
Source0:        http://ftp.edgewall.com/pub/trac/Trac-%{version}.tar.gz
Source2:        trac.ini
Source3:        trac.ini-environment_sample
Source4:        %{name}-README.fedora
Source5:        trac.wsgi

Patch0:         changeset_17861.diff
Patch1:         changeset_17862.diff

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-jinja2
BuildRequires:  python3-markupsafe
BuildRequires:  make

# optional packages to ensure we run all Trac tests (if one of these are not
# installed the test would be skipped)
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  python3-textile
BuildRequires:  python3-subversion
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/svnadmin
# No geckodriver in Fedora, hence we skip the selenium tests
#  BuildRequires:  python3-selenium
#  BuildRequires:  /usr/bin/geckodriver
# No tidylib in Fedora either
#  BuildRequires:  python3-tidylib

%description
Trac is an integrated system for managing software projects, an
enhanced wiki, a flexible web-based issue tracker, and an interface to
the Subversion revision control system.  At the core of Trac lies an
integrated wiki and issue/bug database. Using wiki markup, all objects
managed by Trac can directly link to other issues/bug reports, code
changesets, documentation and files.  Around the core lies other
modules, providing additional features and tools to make software
development more streamlined and effective.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Trac-%{version}

%patch -P 0 -p0
%patch -P 1 -p0

find contrib -type f -exec chmod -x '{}' \;
# don't package windows specific files
rm -f contrib/trac-post-commit-hook.cmd
cp -a %{SOURCE4} README.fedora

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '[Tt]rac*'

install -dm 755 $RPM_BUILD_ROOT%{_var}/www/cgi-bin

install -Dpm 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/trac/trac.ini
install -Dpm 644 %{SOURCE3} $RPM_BUILD_ROOT/etc/trac/trac.ini-environment_sample
install -dpm 755 $RPM_BUILD_ROOT/etc/trac/{plugin,template}s.d

find sample-plugins/ -type f -name '*.py' -exec install -pm 644 '{}' $RPM_BUILD_ROOT/etc/trac/plugins.d \;

find sample-plugins/ -type f -name '*.ini*' -exec install -pm 644 '{}' $RPM_BUILD_ROOT/etc/trac/ \;

install -dm 755 $RPM_BUILD_ROOT%{_sbindir}

#%%check
#PYTHONPATH=$(pwd) PYTHON=/usr/bin/python3 make test

%files -f %{pyproject_files}
%doc AUTHORS ChangeLog INSTALL* README* RELEASE* THANKS UPGRADE* contrib/
%{_bindir}/trac-admin
%{_bindir}/tracd
%dir /etc/trac
%config(noreplace) /etc/trac/*

%changelog
%autochangelog
