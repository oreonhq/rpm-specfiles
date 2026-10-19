%global source0_hash 9fd672b1c8425fac2fa67fa0477b990987268b90ff36d5f016dae57be0d6b52e
%bcond_without autoconf_enables_optional_test
Name:       autoconf
Version:    2.73
Release:        1%{?dist}
License:    GPL-2.0-or-later AND GPL-3.0-or-later AND GPL-3.0-or-later WITH Autoconf-exception-generic-3.0 AND GFDL-1.3-or-later AND FSFAP AND X11 AND LicenseRef-Fedora-Public-Domain
Source0:        https://mirrors.kernel.org/gnu/autoconf/autoconf-%{version}.tar.xz
Source1:    config.site
Source2:    autoconf-init.el
URL:        https://www.gnu.org/software/autoconf/
%if "%{name}" != "autoconf"
%global autoconf %(echo autoconf%{version} | tr -d .)
%global autoconf_enables_emacs 0
%{error:"Each downstream must specify its own /opt namespace"}
Summary:        A GNU tool for automatically configuring source code
%else
%bcond_without autoconf_enables_emacs
%global autoconf %{name}
Summary:        A GNU tool for automatically configuring source code
Provides:   autoconf-latest = %{version}-%{release}
Provides:   %(echo autoconf%{version} | tr -d .) = %{version}-%{release}
%endif
BuildArch:  noarch
%bcond_without check
Requires:           perl(File::Compare)
Requires:           perl-interpreter
Requires:           m4 >= 1.4.14
%if %{with autoconf_enables_emacs}
Requires:           emacs-filesystem
%endif
Requires:           gettext-devel
%if %{with check}
%if %{with autoconf_enables_optional_test}
%endif
%endif
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Autom4te::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Autom4te::
%if "%{name}" != "autoconf"
Requires: %{autoconf}
# oreon:deps
BuildRequires:  emacs
BuildRequires:  erlang
BuildRequires:  gcc-gfortran
BuildRequires:  help2man
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl-generators
BuildRequires:  perl-macros
# /oreon:deps
%description -n autoconf-latest
The latest GNU Autoconf, with a version-specific install
%package -n %{autoconf}
Summary: A GNU tool for automatically configuring source code
%endif
%description -n %{autoconf}
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to
specify various configuration options.

You should install Autoconf if you are developing software and
would like to create shell scripts that configure your source code
packages. If you are installing Autoconf, you will also need to
install the GNU m4 package.

Note that the Autoconf package is not required for the end-user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not
their use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir autoconf-%{version}
%oreon_prep
%build

%if %{with autoconf_enables_emacs}
export EMACS=%{_bindir}/emacs
%else
export EMACS=%{_bindir}/false
%endif
%configure \
    %{?with_autoconf_enables_emacs:--with-lispdir=%{_emacs_sitelispdir}/autoconf}
%make_build
%check

%if %{with check}
case $(./build-aux/config.guess) in
  i?86-*-linux*)
    make check %{?_smp_mflags} TESTSUITEFLAGS="-k '!AC_SYS_LARGEFILE,!AC_SYS_YEAR2038,!AC_SYS_YEAR2038_RECOMMENDED'"
    make check TESTSUITEFLAGS="-k 'AC_SYS_LARGEFILE,AC_SYS_YEAR2038,AC_SYS_YEAR2038_RECOMMENDED'" %{?_smp_mflags} || true
    ;;
  *)
    make check %{?_smp_mflags}
    ;;
esac
%endif
%install
%make_install
mkdir -p %{buildroot}/share
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}
%if %{with autoconf_enables_emacs}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 0644 %{SOURCE2} %{buildroot}%{_emacs_sitestartdir}
%endif
%if "%{name}" != "autoconf"
install -d -m 755 ${RPM_BUILD_ROOT}/etc/scl/prefixes
dirname %{_prefix} > %{autoconf}.prefix
install -p -m 644 %{autoconf}.prefix ${RPM_BUILD_ROOT}/etc/scl/prefixes/%{autoconf}
echo "export PATH=%{_prefix}/bin:\$PATH" > enable.scl
install -p -m 755 enable.scl ${RPM_BUILD_ROOT}/%{_prefix}/enable
%oreon_autofiles main
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
