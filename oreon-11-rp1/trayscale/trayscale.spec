%global source0_hash 57f00bb8a1fa650ac49140ffa1ffbe682e0933b0a411ae94fbf1ff9e97771232
%bcond_without vendor
%if %{without vendor}
%bcond check 0
%endif
%global gomodulesmode GO111MODULE=on
%global goipath         github.com/DeedleFake/trayscale
Version:                0.18.7
%gometa -f
%global common_description %{expand:
An unofficial GUI wrapper around the Tailscale CLI client.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           trayscale
Release:        1%{?dist}
Summary:        An unofficial GUI wrapper around the Tailscale CLI client
License:        MIT AND BSD-2-Clause AND Apache-2.0 AND MPL-2.0 AND ISC AND BSD-3-Clause
URL:            %{gourl}
Source0:        trayscale-%{version}-vendored.tar.xz
Source99:       create-vendor-tarball.sh
Requires:               hicolor-icon-theme
Provides:       bundled(golang(deedles.dev/mk)) = v0.1.0
Provides:       bundled(golang(deedles.dev/tray)) = v0.1.11~0.20251126205835~30c3ecc68b10
Provides:       bundled(golang(deedles.dev/xiter)) = v0.2.1
Provides:       bundled(golang(github.com/diamondburned/gotk4-adwaita/pkg)) = v0.0.0~20250703085337~e94555b846b6
Provides:       bundled(golang(github.com/diamondburned/gotk4/pkg)) = v0.3.2~0.20250703063411~16654385f59a
Provides:       bundled(golang(github.com/inhies/go-bytesize)) = v0.0.0~20220417184213~4913239db9cf
Provides:       bundled(golang(github.com/klauspost/compress)) = v1.18.4
Provides:       bundled(golang(github.com/stretchr/testify)) = v1.11.1
Provides:       bundled(golang(tailscale.com)) = v1.94.1
Provides:       bundled(golang(filippo.io/edwards25519)) = v1.1.0
Provides:       bundled(golang(fyne.io/systray)) = v1.12.0
Provides:       bundled(golang(github.com/BurntSushi/toml)) = v1.5.0
Provides:       bundled(golang(github.com/KarpelesLab/weak)) = v0.1.1
Provides:       bundled(golang(github.com/Kodeworks/golang-image-ico)) = v0.0.0~20141118225523~73f0f4cfade9
Provides:       bundled(golang(github.com/akutz/memconn)) = v0.1.0
Provides:       bundled(golang(github.com/alexbrainman/sspi)) = v0.0.0~20250919150558~7d374ff0d59e
Provides:       bundled(golang(github.com/atotto/clipboard)) = v0.1.4
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2)) = v1.41.1
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/config)) = v1.32.7
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/credentials)) = v1.19.7
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/feature/ec2/imds)) = v1.18.17
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/internal/configsources)) = v1.4.17
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/internal/endpoints/v2)) = v2.7.17
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/internal/ini)) = v1.8.4
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding)) = v1.13.4
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/internal/presigned-url)) = v1.13.17
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/signin)) = v1.0.5
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/ssm)) = v1.66.2
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/sso)) = v1.30.9
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/ssooidc)) = v1.35.13
Provides:       bundled(golang(github.com/aws/aws-sdk-go-v2/service/sts)) = v1.41.6
Provides:       bundled(golang(github.com/aws/smithy-go)) = v1.24.0
Provides:       bundled(golang(github.com/coder/websocket)) = v1.8.14
Provides:       bundled(golang(github.com/coreos/go-iptables)) = v0.8.0
Provides:       bundled(golang(github.com/creachadair/msync)) = v0.8.3
Provides:       bundled(golang(github.com/davecgh/go-spew)) = v1.1.2~0.20180830191138~d8f796af33cc
Provides:       bundled(golang(github.com/dblohm7/wingoes)) = v0.0.0~20250822163801~6d8e6105c62d
Provides:       bundled(golang(github.com/fogleman/gg)) = v1.3.0
Provides:       bundled(golang(github.com/fxamacker/cbor/v2)) = v2.9.0
Provides:       bundled(golang(github.com/gaissmai/bart)) = v0.26.1
Provides:       bundled(golang(github.com/go-json-experiment/json)) = v0.0.0~20251027170946~4849db3c2f7e
Provides:       bundled(golang(github.com/godbus/dbus/v5)) = v5.2.2
Provides:       bundled(golang(github.com/golang/freetype)) = v0.0.0~20170609003504~e2365dfdc4a0
Provides:       bundled(golang(github.com/golang/groupcache)) = v0.0.0~20241129210726~2c02b8208cf8
Provides:       bundled(golang(github.com/google/btree)) = v1.1.3
Provides:       bundled(golang(github.com/google/go-cmp)) = v0.7.0
Provides:       bundled(golang(github.com/google/nftables)) = v0.3.0
Provides:       bundled(golang(github.com/google/uuid)) = v1.6.0
Provides:       bundled(golang(github.com/hdevalence/ed25519consensus)) = v0.2.0
Provides:       bundled(golang(github.com/huin/goupnp)) = v1.3.0
Provides:       bundled(golang(github.com/jsimonetti/rtnetlink)) = v1.4.2
Provides:       bundled(golang(github.com/kballard/go-shellquote)) = v0.0.0~20180428030007~95032a82bc51
Provides:       bundled(golang(github.com/mattn/go-colorable)) = v0.1.14
Provides:       bundled(golang(github.com/mattn/go-isatty)) = v0.0.20
Provides:       bundled(golang(github.com/mdlayher/netlink)) = v1.8.0
Provides:       bundled(golang(github.com/mdlayher/socket)) = v0.5.1
Provides:       bundled(golang(github.com/miekg/dns)) = v1.1.68
Provides:       bundled(golang(github.com/mitchellh/go-ps)) = v1.0.0
Provides:       bundled(golang(github.com/peterbourgon/ff/v3)) = v3.4.0
Provides:       bundled(golang(github.com/pires/go-proxyproto)) = v0.11.0
Provides:       bundled(golang(github.com/pmezard/go-difflib)) = v1.0.1~0.20181226105442~5d4384ee4fb2
Provides:       bundled(golang(github.com/safchain/ethtool)) = v0.7.0
Provides:       bundled(golang(github.com/skip2/go-qrcode)) = v0.0.0~20200617195104~da1b6568686e
Provides:       bundled(golang(github.com/tailscale/certstore)) = v0.1.1~0.20231202035212~d3fa0460f47e
Provides:       bundled(golang(github.com/tailscale/go-winio)) = v0.0.0~20231025203758~c4f33415bf55
Provides:       bundled(golang(github.com/tailscale/hujson)) = v0.0.0~20250605163823~992244df8c5a
Provides:       bundled(golang(github.com/tailscale/peercred)) = v0.0.0~20250107143737~35a0c7bd7edc
Provides:       bundled(golang(github.com/tailscale/web-client-prebuilt)) = v0.0.0~20251127225136~f19339b67368
Provides:       bundled(golang(github.com/tailscale/wireguard-go)) = v0.0.0~20250716170648~1d0488a3d7da
Provides:       bundled(golang(github.com/toqueteos/webbrowser)) = v1.2.1
Provides:       bundled(golang(github.com/x448/float16)) = v0.8.4
Provides:       bundled(golang(go.yaml.in/yaml/v2)) = v2.4.3
Provides:       bundled(golang(go4.org/mem)) = v0.0.0~20240501181205~ae6ca9944745
Provides:       bundled(golang(go4.org/netipx)) = v0.0.0~20231129151722~fdeea329fbba
Provides:       bundled(golang(go4.org/unsafe/assume-no-moving-gc)) = v0.0.0~20231121144256~b99613f794b6
Provides:       bundled(golang(golang.org/x/crypto)) = v0.48.0
Provides:       bundled(golang(golang.org/x/exp)) = v0.0.0~20260209203927~2842357ff358
Provides:       bundled(golang(golang.org/x/exp/typeparams)) = v0.0.0~20250305212735~054e65f0b394
Provides:       bundled(golang(golang.org/x/image)) = v0.36.0
Provides:       bundled(golang(golang.org/x/mod)) = v0.33.0
Provides:       bundled(golang(golang.org/x/net)) = v0.50.0
Provides:       bundled(golang(golang.org/x/oauth2)) = v0.35.0
Provides:       bundled(golang(golang.org/x/sync)) = v0.19.0
Provides:       bundled(golang(golang.org/x/sys)) = v0.41.0
Provides:       bundled(golang(golang.org/x/term)) = v0.40.0
Provides:       bundled(golang(golang.org/x/text)) = v0.34.0
Provides:       bundled(golang(golang.org/x/time)) = v0.14.0
Provides:       bundled(golang(golang.org/x/tools)) = v0.42.0
Provides:       bundled(golang(golang.zx2c4.com/wintun)) = v0.0.0~20230126152724~0fa3db229ce2
Provides:       bundled(golang(golang.zx2c4.com/wireguard/windows)) = v0.5.3
Provides:       bundled(golang(gopkg.in/check.v1)) = v1.0.0~20201130134442~10cb98267c6c
Provides:       bundled(golang(gopkg.in/yaml.v3)) = v3.0.1
Provides:       bundled(golang(gvisor.dev/gvisor)) = v0.0.0~20260210201108~b3aa83da69bd
Provides:       bundled(golang(honnef.co/go/tools)) = v0.7.0~0.dev.0.20251022135355~8273271481d0
Provides:       bundled(golang(k8s.io/client-go)) = v0.35.1
Provides:       bundled(golang(sigs.k8s.io/yaml)) = v1.6.0
Provides:       bundled(golang(software.sslmate.com/src/go-pkcs12)) = v0.7.0
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  cairo-gobject-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  glib2-devel
BuildRequires:  go-rpm-macros
BuildRequires:  gobject-introspection-devel
BuildRequires:  golang
BuildRequires:  graphene-devel
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libappstream-glib
BuildRequires:  pango-devel
# /oreon:deps
%description %{common_description}

%if %{without vendor}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{without vendor}
#rm -rf vendor/
%endif

%goprep %{?with_vendor:-k}

%build

export LDFLAGS="-X 'github.com/DeedleFake/trayscale/version=%{version}'"
%gobuild -o trayscale ./cmd/trayscale
%install
%if %{without vendor}
%gopkginstall
%else
install -D -t %{buildroot}%{_bindir} trayscale
install -Dm644 -t %{buildroot}%{_datadir}/applications dev.deedles.Trayscale.desktop
install -Dm644 -t %{buildroot}%{_datadir}/icons/hicolor/256x256/apps dev.deedles.Trayscale.png
install -Dm644 -t %{buildroot}%{_metainfodir} dev.deedles.Trayscale.metainfo.xml
install -Dm644 -t %{buildroot}%{_datadir}/glib-2.0/schemas dev.deedles.Trayscale.gschema.xml
%oreon_autofiles main
%endif
%check

desktop-file-validate %{buildroot}%{_datadir}/applications/dev.deedles.Trayscale.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/dev.deedles.Trayscale.metainfo.xml
%if %{with check}
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
