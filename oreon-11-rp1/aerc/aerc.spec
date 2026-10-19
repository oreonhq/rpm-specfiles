%global source0_hash 3f1469bbaea982fc58352f2682932ecc2fb50c705994d96b2343e771747745a7
%bcond check 1
%global goipath         git.sr.ht/~rjarry/aerc
%global version0        0.21.0
%gometa -L -f
%global common_description %{expand:
Aerc is an email client that runs in your terminal. It is highly
efficient and extensible, perfect for the discerning hacker.}
Name:           aerc
Version:        %{forgeversion}
Release:        1%{?dist}
Summary:        Email client for your terminal
SourceLicense:  MIT
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version0}.tar.gz#/%{name}-%{version0}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       w3m
Recommends:     git-email
Recommends:     gnupg2
Recommends:     util-linux
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  glibc-all-langpacks
BuildRequires:  gnupg
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
BuildRequires:  notmuch-devel
BuildRequires:  scdoc
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}
%autopatch -p1

%build

%set_build_flags
GO_BUILDTAGS=notmuch GO_LDFLAGS=""
%make_build \
  BUILD_OPTS=%{gobuild_baseflags_shescaped} \
  DATE="$(date -d "@${SOURCE_DATE_EPOCH}" +%Y-%m-%d)" \
  GOFLAGS= \
  GO_EXTRA_LDFLAGS=%{gobuild_ldflags_shescaped} \
  PREFIX=%{_prefix} \
  VERSION=%{version} \
%install
export PREFIX=%{_prefix}
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/aerc.desktop
%go_vendor_license_install -c %{S:2}
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
LANG=en_US.UTF-8 ./filters/test.sh
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
