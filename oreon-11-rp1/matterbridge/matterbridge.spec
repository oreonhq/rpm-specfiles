%global source0_hash 6281eac070661398de74fa32e325c54de85c888cb64d325fe2e0d56d390dcca4
%bcond_without vendor
%if %{without vendor}
%bcond check 0
%endif
%global gomodulesmode GO111MODULE=on
%global goipath         github.com/42wim/matterbridge
Version:                1.26.0
%gometa -f
%global common_description %{expand:
Bridge between mattermost, IRC, xmpp, slack, discord, telegram,
twitch, ssh-chat, zulip, whatsapp, keybase, matrix, microsoft
teams, nextcloud, mumble, vk and more with REST API (mattermost not required!).}
%global golicenses      LICENSE
%global godocs          README.md changelog.md matterclient/README.md
Name:           matterbridge
Release:        1%{?dist}
Summary:        Bridge between many online chat protocols
License:        BSD-2-Clause AND MIT AND (Apache-2.0 OR AGPL-3.0-only) AND Apache-2.0 AND MPL-2.0 AND GPL-3.0-or-later AND ISC AND (MIT OR ICU) AND BSD-3-Clause
URL:            %{gourl}
Source0:        %{name}-%{version}-vendored.tar.xz
Source1:        %{name}.service
Source2:	%{name}.toml
Source3:        %{name}.sysusers
Source9:        create-vendor-tarball.sh
Provides:       bundled(golang(github.com/42wim/go-gitter)) = v0.0.0~20170828205020~017310c2d557
Provides:       bundled(golang(github.com/Baozisoftware/qrcode-terminal-go)) = v0.0.0~20170407111555~c0650d8dff0f
Provides:       bundled(golang(github.com/Benau/tgsconverter)) = v0.0.0~20210809170556~99f4a4f6337f
Provides:       bundled(golang(github.com/Philipp15b/go-steam)) = v1.0.1~0.20200727090957~6ae9b3c0a560
Provides:       bundled(golang(github.com/Rhymen/go-whatsapp)) = v0.1.2~0.20211102134409~31a2e740845c
Provides:       bundled(golang(github.com/SevereCloud/vksdk/v2)) = v2.15.0
Provides:       bundled(golang(github.com/bwmarrin/discordgo)) = v0.27.0
Provides:       bundled(golang(github.com/d5/tengo/v2)) = v2.13.0
Provides:       bundled(golang(github.com/davecgh/go-spew)) = v1.1.1
Provides:       bundled(golang(github.com/fsnotify/fsnotify)) = v1.6.0
Provides:       bundled(golang(github.com/go-telegram-bot-api/telegram-bot-api/v5)) = v5.5.1
Provides:       bundled(golang(github.com/gomarkdown/markdown)) = v0.0.0~20221013030248~663e2500819c
Provides:       bundled(golang(github.com/google/gops)) = v0.3.26
Provides:       bundled(golang(github.com/gorilla/schema)) = v1.2.0
Provides:       bundled(golang(github.com/gorilla/websocket)) = v1.5.0
Provides:       bundled(golang(github.com/hashicorp/golang-lru)) = v0.6.0
Provides:       bundled(golang(github.com/jpillora/backoff)) = v1.0.0
Provides:       bundled(golang(github.com/keybase/go-keybase-chat-bot)) = v0.0.0~20221220212439~e48d9abd2c20
Provides:       bundled(golang(github.com/kyokomi/emoji/v2)) = v2.2.11
Provides:       bundled(golang(github.com/labstack/echo/v4)) = v4.10.0
Provides:       bundled(golang(github.com/lrstanley/girc)) = v0.0.0~20221222153823~a92667a5c9b4
Provides:       bundled(golang(github.com/matterbridge/Rocket.Chat.Go.SDK)) = v0.0.0~20211016222428~79310a412696
Provides:       bundled(golang(github.com/matterbridge/go-xmpp)) = v0.0.0~20211030125215~791a06c5f1be
Provides:       bundled(golang(github.com/matterbridge/gomatrix)) = v0.0.0~20220411225302~271e5088ea27
Provides:       bundled(golang(github.com/matterbridge/gozulipbot)) = v0.0.0~20211023205727~a19d6c1f3b75
Provides:       bundled(golang(github.com/matterbridge/logrus-prefixed-formatter)) = v0.5.3~0.20200523233437~d971309a77ba
Provides:       bundled(golang(github.com/matterbridge/matterclient)) = v0.0.0~20220624224459~272af20c7ddf
Provides:       bundled(golang(github.com/mattermost/mattermost-server/v5)) = v5.39.3
Provides:       bundled(golang(github.com/mattermost/mattermost-server/v6)) = v6.7.2
Provides:       bundled(golang(github.com/mattn/godown)) = v0.0.1
Provides:       bundled(golang(github.com/mdp/qrterminal)) = v1.0.1
Provides:       bundled(golang(github.com/paulrosania/go-charset)) = v0.0.0~20190326053356~55c9d7a5834c
Provides:       bundled(golang(github.com/rs/xid)) = v1.4.0
Provides:       bundled(golang(github.com/russross/blackfriday)) = v1.6.0
Provides:       bundled(golang(github.com/saintfish/chardet)) = v0.0.0~20230101081208~5e3ef4b5456d
Provides:       bundled(golang(github.com/shazow/ssh-chat)) = v1.10.1
Provides:       bundled(golang(github.com/sirupsen/logrus)) = v1.9.0
Provides:       bundled(golang(github.com/slack-go/slack)) = v0.12.1
Provides:       bundled(golang(github.com/spf13/viper)) = v1.15.0
Provides:       bundled(golang(github.com/stretchr/testify)) = v1.8.1
Provides:       bundled(golang(github.com/vincent-petithory/dataurl)) = v1.0.0
Provides:       bundled(golang(github.com/writeas/go-strip-markdown)) = v2.0.1+incompatible
Provides:       bundled(golang(github.com/yaegashi/msgraph.go)) = v0.1.4
Provides:       bundled(golang(github.com/zfjagann/golang-ring)) = v0.0.0~20220330170733~19bcea1b6289
Provides:       bundled(golang(go.mau.fi/whatsmeow)) = v0.0.0~20230128195103~dcbc8dd31a22
Provides:       bundled(golang(golang.org/x/image)) = v0.3.0
Provides:       bundled(golang(golang.org/x/oauth2)) = v0.4.0
Provides:       bundled(golang(golang.org/x/text)) = v0.6.0
Provides:       bundled(golang(gomod.garykim.dev/nc-talk)) = v0.3.0
Provides:       bundled(golang(google.golang.org/protobuf)) = v1.28.1
Provides:       bundled(golang(gopkg.in/olahol/melody.v1)) = v1.0.0~20170518105555~d52139073376
Provides:       bundled(golang(layeh.com/gumble)) = v0.0.0~20221205141517~d1df60a3cc14
Provides:       bundled(golang(modernc.org/sqlite)) = v1.20.3
Provides:       bundled(golang(filippo.io/edwards25519)) = v1.0.0
Provides:       bundled(golang(github.com/Benau/go_rlottie)) = v0.0.0~20210807002906~98c1b2421989
Provides:       bundled(golang(github.com/Jeffail/gabs)) = v1.4.0
Provides:       bundled(golang(github.com/apex/log)) = v1.9.0
Provides:       bundled(golang(github.com/av-elier/go-decimal-to-rational)) = v0.0.0~20191127152832~89e6aad02ecf
Provides:       bundled(golang(github.com/blang/semver)) = v3.5.1+incompatible
Provides:       bundled(golang(github.com/dustin/go-humanize)) = v1.0.0
Provides:       bundled(golang(github.com/dyatlov/go-opengraph)) = v0.0.0~20210112100619~dae8665a5b09
Provides:       bundled(golang(github.com/francoispqt/gojay)) = v1.2.13
Provides:       bundled(golang(github.com/go-asn1-ber/asn1-ber)) = v1.5.3
Provides:       bundled(golang(github.com/golang-jwt/jwt)) = v3.2.2+incompatible
Provides:       bundled(golang(github.com/golang/protobuf)) = v1.5.2
Provides:       bundled(golang(github.com/google/uuid)) = v1.3.0
Provides:       bundled(golang(github.com/gopackage/ddp)) = v0.0.3
Provides:       bundled(golang(github.com/graph-gophers/graphql-go)) = v1.3.0
Provides:       bundled(golang(github.com/hashicorp/errwrap)) = v1.1.0
Provides:       bundled(golang(github.com/hashicorp/go-multierror)) = v1.1.1
Provides:       bundled(golang(github.com/hashicorp/hcl)) = v1.0.0
Provides:       bundled(golang(github.com/json-iterator/go)) = v1.1.12
Provides:       bundled(golang(github.com/kballard/go-shellquote)) = v0.0.0~20180428030007~95032a82bc51
Provides:       bundled(golang(github.com/kettek/apng)) = v0.0.0~20191108220231~414630eed80f
Provides:       bundled(golang(github.com/klauspost/compress)) = v1.15.8
Provides:       bundled(golang(github.com/klauspost/cpuid/v2)) = v2.0.12
Provides:       bundled(golang(github.com/labstack/gommon)) = v0.4.0
Provides:       bundled(golang(github.com/magiconair/properties)) = v1.8.7
Provides:       bundled(golang(github.com/mattermost/go-i18n)) = v1.11.1~0.20211013152124~5c415071e404
Provides:       bundled(golang(github.com/mattermost/ldap)) = v0.0.0~20201202150706~ee0e6284187d
Provides:       bundled(golang(github.com/mattermost/logr)) = v1.0.13
Provides:       bundled(golang(github.com/mattermost/logr/v2)) = v2.0.15
Provides:       bundled(golang(github.com/mattn/go-colorable)) = v0.1.13
Provides:       bundled(golang(github.com/mattn/go-isatty)) = v0.0.16
Provides:       bundled(golang(github.com/mattn/go-runewidth)) = v0.0.13
Provides:       bundled(golang(github.com/mgutz/ansi)) = v0.0.0~20200706080929~d51e80ef957d
Provides:       bundled(golang(github.com/minio/md5-simd)) = v1.1.2
Provides:       bundled(golang(github.com/minio/minio-go/v7)) = v7.0.24
Provides:       bundled(golang(github.com/minio/sha256-simd)) = v1.0.0
Provides:       bundled(golang(github.com/mitchellh/go-homedir)) = v1.1.0
Provides:       bundled(golang(github.com/mitchellh/mapstructure)) = v1.5.0
Provides:       bundled(golang(github.com/modern-go/concurrent)) = v0.0.0~20180306012644~bacd9c7ef1dd
Provides:       bundled(golang(github.com/modern-go/reflect2)) = v1.0.2
Provides:       bundled(golang(github.com/monaco-io/request)) = v1.0.5
Provides:       bundled(golang(github.com/mreiferson/go-httpclient)) = v0.0.0~20201222173833~5e475fde3a4d
Provides:       bundled(golang(github.com/opentracing/opentracing-go)) = v1.2.0
Provides:       bundled(golang(github.com/pborman/uuid)) = v1.2.1
Provides:       bundled(golang(github.com/pelletier/go-toml)) = v1.9.5
Provides:       bundled(golang(github.com/pelletier/go-toml/v2)) = v2.0.6
Provides:       bundled(golang(github.com/philhofer/fwd)) = v1.1.1
Provides:       bundled(golang(github.com/pkg/errors)) = v0.9.1
Provides:       bundled(golang(github.com/pmezard/go-difflib)) = v1.0.0
Provides:       bundled(golang(github.com/remyoudompheng/bigfft)) = v0.0.0~20200410134404~eec4a21b6bb0
Provides:       bundled(golang(github.com/rickb777/date)) = v1.12.4
Provides:       bundled(golang(github.com/rickb777/plural)) = v1.2.0
Provides:       bundled(golang(github.com/rivo/uniseg)) = v0.2.0
Provides:       bundled(golang(github.com/shazow/rateio)) = v0.0.0~20200113175441~4461efc8bdc4
Provides:       bundled(golang(github.com/sizeofint/webpanimation)) = v0.0.0~20210809145948~1d2b32119882
Provides:       bundled(golang(github.com/skip2/go-qrcode)) = v0.0.0~20190110000554~dc11ecdae0a9
Provides:       bundled(golang(github.com/spf13/afero)) = v1.9.3
Provides:       bundled(golang(github.com/spf13/cast)) = v1.5.0
Provides:       bundled(golang(github.com/spf13/jwalterweatherman)) = v1.1.0
Provides:       bundled(golang(github.com/spf13/pflag)) = v1.0.5
Provides:       bundled(golang(github.com/subosito/gotenv)) = v1.4.2
Provides:       bundled(golang(github.com/tinylib/msgp)) = v1.1.6
Provides:       bundled(golang(github.com/valyala/bytebufferpool)) = v1.0.0
Provides:       bundled(golang(github.com/valyala/fasttemplate)) = v1.2.2
Provides:       bundled(golang(github.com/vmihailenco/msgpack/v5)) = v5.3.5
Provides:       bundled(golang(github.com/vmihailenco/tagparser/v2)) = v2.0.0
Provides:       bundled(golang(github.com/wiggin77/cfg)) = v1.0.2
Provides:       bundled(golang(github.com/wiggin77/merror)) = v1.0.3
Provides:       bundled(golang(github.com/wiggin77/srslog)) = v1.0.1
Provides:       bundled(golang(go.mau.fi/libsignal)) = v0.1.0
Provides:       bundled(golang(go.uber.org/atomic)) = v1.9.0
Provides:       bundled(golang(go.uber.org/multierr)) = v1.8.0
Provides:       bundled(golang(go.uber.org/zap)) = v1.21.0
Provides:       bundled(golang(golang.org/x/crypto)) = v0.4.0
Provides:       bundled(golang(golang.org/x/mod)) = v0.6.0~dev.0.20220419223038~86c51ed26bb4
Provides:       bundled(golang(golang.org/x/net)) = v0.5.0
Provides:       bundled(golang(golang.org/x/sys)) = v0.4.0
Provides:       bundled(golang(golang.org/x/term)) = v0.4.0
Provides:       bundled(golang(golang.org/x/time)) = v0.2.0
Provides:       bundled(golang(golang.org/x/tools)) = v0.1.12
Provides:       bundled(golang(google.golang.org/appengine)) = v1.6.7
Provides:       bundled(golang(gopkg.in/ini.v1)) = v1.67.0
Provides:       bundled(golang(gopkg.in/natefinch/lumberjack.v2)) = v2.0.0
Provides:       bundled(golang(gopkg.in/yaml.v2)) = v2.4.0
Provides:       bundled(golang(gopkg.in/yaml.v3)) = v3.0.1
Provides:       bundled(golang(lukechampine.com/uint128)) = v1.2.0
Provides:       bundled(golang(modernc.org/cc/v3)) = v3.40.0
Provides:       bundled(golang(modernc.org/ccgo/v3)) = v3.16.13
Provides:       bundled(golang(modernc.org/libc)) = v1.22.2
Provides:       bundled(golang(modernc.org/mathutil)) = v1.5.0
Provides:       bundled(golang(modernc.org/memory)) = v1.4.0
Provides:       bundled(golang(modernc.org/opt)) = v0.1.3
Provides:       bundled(golang(modernc.org/strutil)) = v1.1.3
Provides:       bundled(golang(modernc.org/token)) = v1.0.1
Provides:       bundled(golang(rsc.io/qr)) = v0.2.0
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description %{common_description}

%if %{without vendor}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{without vendor}
rm -rf vendor/
%endif

%goprep %{?with_vendor:-k}
%autopatch -p1

%build

export tags="noharmony nogitter norocketchat"
export GO_BUILDTAGS="$GO_BUILDTAGS $tags"
%gobuild -o %{name} ./matterbridge.go
%install
%if %{without vendor}
%gopkginstall
%else
install -D -t %{buildroot}%{_bindir} matterbridge
%endif
mkdir -p %{buildroot}%{_unitdir}
install -pm644 %{S:1} %{buildroot}%{_unitdir}
install -pDm640 %{S:2}  %{buildroot}%{_sysconfdir}/%{name}/%{name}.toml
install -p -D -m 0644 %{S:3} %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles main

%pre

%sysusers_create_compat %{S:3}
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
