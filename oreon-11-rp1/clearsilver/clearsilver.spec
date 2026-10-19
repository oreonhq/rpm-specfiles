%global source0_hash 1e9da038deafddd3d0c1c510626c28be5a0f4f17b9091d577fd30e7c5ba88680
Name:           clearsilver
Version:        0.11.0
Release:        1%{?dist}
Summary:        Fast and powerful HTML templating system
License:        Apache-1.1
URL:            http://www.clearsilver.net/
Source0:        http://www.clearsilver.net/downloads/%{name}-%{version}.tar.gz
Patch0:         clearsilver-0.10.5-fedora.patch
Patch1:         clearsilver-0.10.5-regression.patch
Patch2:         clearsilver-0.10.5-CVE-2011-4357.patch
Patch3:         clearsilver-ruby-1.9.patch
Patch4:         clearsilver-ruby-2.2.patch
Patch5:         clearsilver-0.10.5-gcc5.patch
Patch6:         clearsilver-configure-c99.patch
Patch7:         pointers.patch
Patch8:         overflow.patch
ExcludeArch:    %{ix86}
Conflicts:      python3-cs
# oreon:deps
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  ruby
BuildRequires:  ruby-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd cs
make clean
make test
popd
%files -f %{oreon_filedir}/main.list
%files -n clearsilver-devel -f %{oreon_filedir}/clearsilver-devel.list
%files -n perl-clearsilver -f %{oreon_filedir}/perl-clearsilver.list
%files -n ruby-clearsilver -f %{oreon_filedir}/ruby-clearsilver.list

%changelog

%autochangelog
