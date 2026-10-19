%global source0_hash dd343b63ecbe2170a82a7253d03325279fecc0d70f607eb738f012a45d523d82
%global forgeurl    https://bitbucket.org/gbcox/transflac/
%global commit      6b689cf7f5d1
Name:           transflac
Version:        1.2.7
Summary:        Transcode FLAC to lossy formats
License:        GPL-3.0-or-later
%{forgemeta}
URL:            %{forgeurl}
Release:        1%{?dist}
Source0:        %{forgeurl}get/%{commit}.tar.bz2#/gbcox-%{name}-%{commit}.tar.bz2
Source1:        %{name}.rpmlintrc
BuildArch:      noarch
Requires:       figlet
Requires:       flac
Requires:       vorbis-tools
Requires:       opus-tools
Requires:       rsync
Requires:       procps-ng
Requires:       coreutils
Requires:       (ffmpeg or ffmpeg-free)
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
transflac is a front end command line utility (actually, a bash script)
that transcodes FLAC audio files into various lossy formats.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{forgesetup}
%autosetup -n %{archivename}

%build

%install
%make_install prefix=%{_prefix} sysconfdir=%{_sysconfdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
