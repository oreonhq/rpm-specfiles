%global source0_hash 5d276d42d3b78827f975cf33aefee13c70ce549c4a7479f191fc6899a5692642
Name:           devscripts
Version:        2.26.12
Release:        1%{?dist}
Summary:        Scripts for Debian Package maintainers
BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/%{name}
Source0:        http://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
Patch0:         devscripts_docbook.patch
Patch1:         devscripts_install-layout.patch
Patch2:         devscripts_install-man.patch
Requires:       dpkg-dev
Requires:       sensible-utils
Requires:       %{_bindir}/man
Requires:       %{name}-checkbashisms
# oreon:deps
BuildRequires:  /usr/bin/dpkg-buildflags
BuildRequires:  /usr/bin/dpkg-parsechangelog
BuildRequires:  /usr/bin/dpkg-vendor
BuildRequires:  /usr/bin/help2man
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Data::Dumper)
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
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::DesktopEntry)
BuildRequires:  perl(File::DirList)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Git::Wrapper)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Compare)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Parse::DebControl)
BuildRequires:  perl(Pod::Checker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(filetest)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  po4a
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Scripts to make the life of a Debian Package maintainer easier.

%package checkbashisms
Summary:        Devscripts checkbashisms script
%description checkbashisms
This package contains the devscripts checkbashisms script.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir devscripts
%oreon_prep
%build

%make_build
%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc
rm %{buildroot}%{_bindir}/archpath %{buildroot}%{_mandir}/man1/archpath*
rm %{buildroot}%{_bindir}/whodepends %{buildroot}%{_mandir}/man1/whodepends*
ln -s %{_bindir}/cvs-debi      %{buildroot}%{_bindir}/cvs-debc
ln -s %{_bindir}/debchange     %{buildroot}%{_bindir}/dch
ln -s %{_bindir}/pts-subscribe %{buildroot}%{_bindir}/pts-unsubscribe
ln -s %{_mandir}/man1/debchange.1.gz     %{buildroot}%{_mandir}/man1/dch.1.gz
ln -s %{_mandir}/man1/pts-subscribe.1.gz %{buildroot}%{_mandir}/man1/pts-unsubscribe.1.gz
rm -f %{buildroot}%{_datadir}/bash-completion/completions/bts
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n devscripts-checkbashisms -f %{oreon_filedir}/devscripts-checkbashisms.list

%changelog

%autochangelog
