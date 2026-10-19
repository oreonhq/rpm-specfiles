%global source0_hash 9a70383143b6e3f43ee079f551b7f5719037ada86eb48d9defc66e00e619d996
Name:           get_iplayer
Version:        3.36
Release:        1%{?dist}
Summary:        Lists, records and streams BBC iPlayer TV and radio programmes
License:        GPL-3.0-or-later
URL:            https://github.com/get-iplayer/%{name}
Source0:        https://github.com/get-iplayer/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       /usr/bin/ffmpeg
Requires:       AtomicParsley
Requires:       perl-interpreter
Requires:       perl(Encode::Locale)
Requires:       perl(Mojolicious) >= 4.63
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Env)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(LWP::ConnCache)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PerlIO::encoding)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(open)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
get_iplayer is a tool for listing, recording and streaming BBC iPlayer
television and radio programmes, and other programmes via 3rd-party
plugins.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./get_iplayer --manpage=get_iplayer.1 || :
%install
install -Dpm0755 -t %{buildroot}%{_bindir} get_iplayer
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 get_iplayer.1
touch options
install -Dpm0644 -t %{buildroot}%{_sysconfdir}/get_iplayer options
install -Dpm0644 -t %{buildroot}%{_datadir}/mime/packages %{SOURCE1}
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications %{SOURCE2}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
