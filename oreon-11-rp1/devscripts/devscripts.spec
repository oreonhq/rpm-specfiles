%global source0_hash bd57069293354cb973b4a09b5f980f15382082680e1eb0bd90d32c555330a211

Name:           devscripts
Version:        2.26.5
Release:        1%{?dist}
Summary:        Scripts for Debian Package maintainers
BuildArch:      noarch

License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/%{name}
Source0:        http://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
# Fixes path to xsl-stylesheet manpages docbook.xsl
Patch0:         devscripts_docbook.patch
# Removes the debian-only --install-layout python-setuptools option
Patch1:         devscripts_install-layout.patch
# Install some additional man pages
Patch2:         devscripts_install-man.patch

BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Dpkg::Changelog::Debian)
BuildRequires:  perl(Dpkg::Changelog::Parse)
BuildRequires:  perl(Dpkg::Control)
BuildRequires:  perl(Dpkg::Control::Hash)
BuildRequires:  perl(Dpkg::Vendor)
BuildRequires:  perl(Dpkg::Version)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::DesktopEntry)
BuildRequires:  perl(File::DirList)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(filetest)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Git::Wrapper)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Compare)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(open)
BuildRequires:  perl(Parse::DebControl)
BuildRequires:  perl(Pod::Checker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(URI) >= 1.37
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
BuildRequires:  po4a
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  /usr/bin/dpkg-buildflags
BuildRequires:  /usr/bin/dpkg-vendor
BuildRequires:  /usr/bin/dpkg-parsechangelog
BuildRequires:  /usr/bin/help2man
BuildRequires:  pkgconfig(bash-completion)

Requires:       dpkg-dev
Requires:       sensible-utils
# man for manpage-alert
Requires:       %{_bindir}/man
Requires:       %{name}-checkbashisms

%description
Scripts to make the life of a Debian Package maintainer easier.

%package checkbashisms
Summary:        Devscripts checkbashisms script

%description checkbashisms
This package contains the devscripts checkbashisms script.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -C

%build
%make_build

%install
%make_install

# Install docs through %%doc
rm -rf %{buildroot}%{_datadir}/doc

# archpath requires tla (gnu-arch) or baz (bazaar), both of which are obsolete
# and the respective Fedora packages dead. See #1128503
rm %{buildroot}%{_bindir}/archpath %{buildroot}%{_mandir}/man1/archpath*

# whodepends requires configured deb repositories
rm %{buildroot}%{_bindir}/whodepends %{buildroot}%{_mandir}/man1/whodepends*

# Create symlinks like the debian package does
ln -s %{_bindir}/cvs-debi      %{buildroot}%{_bindir}/cvs-debc
ln -s %{_bindir}/debchange     %{buildroot}%{_bindir}/dch
ln -s %{_bindir}/pts-subscribe %{buildroot}%{_bindir}/pts-unsubscribe
ln -s %{_mandir}/man1/debchange.1.gz     %{buildroot}%{_mandir}/man1/dch.1.gz
ln -s %{_mandir}/man1/pts-subscribe.1.gz %{buildroot}%{_mandir}/man1/pts-unsubscribe.1.gz

# This already is in bash-completion
rm -f %{buildroot}%{_datadir}/bash-completion/completions/bts

%files
%doc README.md
%license COPYING
%{_datadir}/bash-completion
%{_bindir}/*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}*.egg-info/
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_mandir}/man7/*
%{perl_vendorlib}/Devscripts
%exclude %{_bindir}/checkbashisms
%exclude %{_mandir}/man1/checkbashisms.1*
%exclude %{_datadir}/bash-completion/completions/checkbashisms

%files checkbashisms
%license COPYING
%{_bindir}/checkbashisms
%{_mandir}/man1/checkbashisms.1*
%{_mandir}/man5/devscripts.conf.5*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/checkbashisms

%changelog
%autochangelog
