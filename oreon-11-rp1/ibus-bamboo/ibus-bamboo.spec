%global source0_hash 610031553a033cde9f0c8bb08fd8578763611f24964566973997d7ae57a3c99e
%global source_version %%(echo "%version" | tr '~' '-')
%global main_version %%(echo "%version" | sed -e 's/~.*//')
%global debug_package %{nil}
%global _build_go_ldflags -ldflags '-w -s -X main.Version=%{main_version}'
%global build_goflags %{?build_goflags}%{!?build_goflags:%_build_go_ldflags -trimpath -buildmode=pie}
Name: ibus-bamboo
Version: 0.8.4~RC6
Release:        1%{?dist}
Summary:        A Vietnamese input method for IBus
License: GPL-3.0-or-later and MIT
URL: https://github.com/BambooEngine/ibus-bamboo
Source0:        https://github.com/BambooEngine/%{name}/archive/refs/tags/v0.8.4-RC6.tar.gz#/%{name}-0.8.4-RC6.tar.gz
Source1: bamboo.xml
Source2: us.xml
Source3: others.xml
Patch1:  %{name}-2402676-del-attr-none.patch
Patch2:  %{name}-2430316-engine-xml.patch
Requires:       gtk3
Requires:       ibus
Requires:       %{name}-engine-vi-us = %{version}-%{release}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  go
BuildRequires:  gtk3-devel
BuildRequires:  ibus-devel
BuildRequires:  libX11-devel
BuildRequires:  libXtst-devel
# /oreon:deps
%description
A Vietnamese IME for IBus using Bamboo Engine.
The open source Vietnamese keyboard supports most common encodings, popular
Vietnamese typing methods, smart diacritics, spell checking, shortcuts,...

%description -l vi
A Vietnamese IME for IBus using Bamboo Engine.
Bộ gõ tiếng Việt mã nguồn mở hỗ trợ hầu hết các bảng mã thông dụng, các kiểu
gõ tiếng Việt phổ biến, bỏ dấu thông minh, kiểm tra chính tả, gõ tắt,...

%package engine-vi-us
Summary:        Vietnamese input method US layout engines of ibus-bamboo
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description engine-vi-us
This includes Vietnamese input-method engines with the Vietnamese language and
the US keyboard layout of %{name}

%package engine-others
Summary:        Miscellaneous Vietnamese input method engines of ibus-bamboo
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description engine-others
This includes Vietnamese input-method engines with the Vietnamese language and
the default keyboard layout, and the English language and the US keyboard
layout except for %{name}-engine-vi-us

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{source_version}
for data in data/bamboo.xml data/ibus-setup-Bamboo.desktop
do
    sed -i.orig -s "s|/lib/ibus-bamboo/|/libexec/|" $data
done

%build

GOLDFLAGS="${GOLDFLAGS:-%{?build_goflags}}"
%{make_build} GOLDFLAGS="$GOLDFLAGS"
%install
GOLDFLAGS="${GOLDFLAGS:-%{?build_goflags}}"
%{make_install} GOLDFLAGS="$GOLDFLAGS"
desktop-file-install --delete-original          \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/*
mv ${RPM_BUILD_ROOT}%{_prefix}/lib/%{name} ${RPM_BUILD_ROOT}%{_libexecdir}
rm ${RPM_BUILD_ROOT}%{_datadir}/%{name}/data/COPYING.emojione
rm ${RPM_BUILD_ROOT}%{_datadir}/%{name}/data/LICENSE.vietnamese.cm.dict
rm ${RPM_BUILD_ROOT}%{_datadir}/%{name}/data/bamboo.xml*
rm ${RPM_BUILD_ROOT}%{_datadir}/%{name}/data/ibus-bamboo.spec
rm ${RPM_BUILD_ROOT}%{_datadir}/%{name}/data/ibus-setup-Bamboo.desktop*
diff %SOURCE1 ${RPM_BUILD_ROOT}%{_datadir}/ibus/component/bamboo.xml || :
install -pm 644 -D %SOURCE1 ${RPM_BUILD_ROOT}%{_datadir}/ibus/component/bamboo.xml
install -m 755 -d ${RPM_BUILD_ROOT}%{_datadir}/%{name}/engines
install -pm 644 -D %SOURCE2 ${RPM_BUILD_ROOT}%{_datadir}/%{name}/engines/us.xml
install -pm 644 -D %SOURCE3 ${RPM_BUILD_ROOT}%{_datadir}/%{name}/engines/others.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

CGO_ENABLED=1 go test ./... -mod=vendor
CGO_ENABLED=1 go test ./vendor/github.com/BambooEngine/bamboo-core/... -mod=vendor
%transfiletriggerin -- %{_datadir}/ibus/component
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :
%transfiletriggerpostun -- %{_datadir}/ibus/component
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :
%transfiletriggerin engine-vi-us -- %{_datadir}/%{name}/engines
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :
%transfiletriggerpostun engine-vi-us -- %{_datadir}/%{name}/engines
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :
%transfiletriggerin engine-others -- %{_datadir}/%{name}/engines
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :
%transfiletriggerpostun engine-others -- %{_datadir}/%{name}/engines
[ -x %{_bindir}/ibus ] && \
  %{_bindir}/ibus write-cache --system &>/dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n ibus-bamboo-engine-vi-us -f %{oreon_filedir}/ibus-bamboo-engine-vi-us.list
%files -n ibus-bamboo-engine-others -f %{oreon_filedir}/ibus-bamboo-engine-others.list

%changelog

%autochangelog
