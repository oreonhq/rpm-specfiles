%global source0_hash 0fa53d78aa164dda98aa16bc1b25ed06fc6b93e6440a80e511b48f07bbd5323d

# Add a rebuild comment to force a new build
#
# This commit forces a rebuild due to infrastructure changes or similar.
# No functional changes are present in this commit.

%global project beetpost
%global goipath codeberg.org/gbcox/%{project}
%global forgeurl https://codeberg.org/gbcox/%{project}/
%global commit a22160cd7f2140e39af22fa35c3064e82f8be3b5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global golicenses LICENSE.md
%global godocs     README.md

%global common_description %{expand:
%{project} is an optional service designed to bridge
the gap between your local media playback and
Beetbrainz.}

%gometa

Name:           %{goname}
Version:        1.7.1
Release:        %autorelease
Summary:        Playback Event Dispatcher for Beetbrainz
License:        GPL-3.0-or-later
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang >= 1.24
BuildRequires: systemd-rpm-macros
BuildRequires: golang(github.com/godbus/dbus/v5)

Provides:      golang-codeberg-gbcox-mpris-webhook = %{version}-%{release}
Obsoletes:     golang-codeberg-gbcox-mpris-webhook < 1.1.6-1.20250714git682a1dd

%description %common_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%generate_buildrequires
%go_generate_buildrequires

%build

export GOFLAGS="-mod=readonly"

export LDFLAGS="\
  -X main.AppVersionFull=%{version} \
  -X main.CommitFull=%{commit} \
  -X main.ShortCommitFull=%{shortcommit} \
  -linkmode external -extldflags '-pie -fPIE %{build_ldflags}'"

%gobuild -o %{project} .

%install
install -Dm755 %{project} %{buildroot}%{_bindir}/%{project}
install -Dm644 %{project}.service %{buildroot}%{_userunitdir}/%{project}.service
mkdir -p %{buildroot}%{_mandir}/man8
install -m644 -p %{project}.8 %{buildroot}%{_mandir}/man8

%check
%{buildroot}%{_bindir}/%{project} --version

%post
%systemd_user_post %{project}.service

%preun
%systemd_user_preun %{project}.service

%postun
%systemd_user_postun %{project}.service

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/%{project}
%{_userunitdir}/%{project}.service
%{_mandir}/man8/%{project}.8*

%changelog
%autochangelog
