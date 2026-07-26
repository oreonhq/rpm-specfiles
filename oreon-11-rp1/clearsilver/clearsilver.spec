%global source0_hash 1e9da038deafddd3d0c1c510626c28be5a0f4f17b9091d577fd30e7c5ba88680

Name:           clearsilver
Version:        0.10.5
Release:        82%{?dist}
Summary:        Fast and powerful HTML templating system
# Technically, the license is "Neotonic ClearSilver", but it is a copy of 
# ASL 1.1 with the trademarks as the only difference.
License:        Apache-1.1
URL:            http://www.clearsilver.net/
Source0:        http://www.clearsilver.net/downloads/%{name}-%{version}.tar.gz
Patch0:         clearsilver-0.10.5-fedora.patch
Patch1:         clearsilver-0.10.5-regression.patch
Patch2:         clearsilver-0.10.5-CVE-2011-4357.patch
Patch3:         clearsilver-ruby-1.9.patch
Patch4:         clearsilver-ruby-2.2.patch
# GCC 5 compatibility, bug #1190760
Patch5:         clearsilver-0.10.5-gcc5.patch
Patch6:         clearsilver-configure-c99.patch
Patch7:         pointers.patch
Patch8:         overflow.patch
BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  httpd-devel

ExcludeArch:    %{ix86}

# both packages have /usr/bin/cs
Conflicts:      python3-cs

%description
ClearSilver is a fast, powerful, and language-neutral HTML template
system.  In both static content sites and dynamic HTML applications,
it provides a separation between presentation code and application
logic which makes working with your project easier.  The design of
ClearSilver began in 1999, and evolved during its use at onelist.com,
egroups.com, and Yahoo! Groups.  Today many other projects and
websites are using it.

%package        devel
Summary:        ClearSilver development package
Provides:       %{name}-static = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides needed files to develop extensions
to ClearSilver.

%package     -n perl-%{name}
Summary:        Perl interface to the ClearSilver HTML templating system
License:        GPL-2.0-only OR Apache-1.1
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
%if 0%{?rhel}
BuildRequires:  perl-ExtUtils-MakeMaker
%endif
Provides:       %{name}-perl = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n perl-%{name}
%{summary}.

%package     -n ruby-%{name}
Summary:        Ruby interface to the ClearSilver HTML templating system
License:        LGPL-2.0-only
BuildRequires:  ruby
BuildRequires:  ruby-devel
Provides:       %{name}-ruby = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n ruby-%{name}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
touch configure
sed -i -r 's|(\$\(RUBY\) install.rb config) (--.*)|\1 --rb-dir="$(DESTDIR)%{ruby_vendorlibdir}" --so-dir="$(DESTDIR)%{ruby_vendorarchdir}" \2|' ruby/Makefile

%build
%configure \
  --disable-java \
  --disable-csharp
%make_build
cd perl && %{__perl} Makefile.PL INSTALLDIRS=vendor && cd ..

%install
%make_install
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name perllocal.pod -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -delete
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
pushd cs
make clean
make test
popd

%files
%doc README
%license CS_LICENSE LICENSE
%{_bindir}/cs
%{_bindir}/cstest
%{_bindir}/cs_static.cgi
%{_mandir}/man3/*

%files devel
%{_includedir}/ClearSilver/
%{_libdir}/libneo_*.a

%files -n perl-clearsilver
%{perl_vendorarch}/auto/ClearSilver/
%{perl_vendorarch}/ClearSilver.pm

%files -n ruby-clearsilver
%{ruby_vendorarchdir}/hdf.so
%{ruby_vendorlibdir}/neo.rb

%changelog
%autochangelog
