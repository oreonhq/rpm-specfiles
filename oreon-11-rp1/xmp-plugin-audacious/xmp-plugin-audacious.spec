%global source0_hash 5f5146b227cc87c7983d9945114084041abc1a99645dd560e0b8c4ba9ea47862

# 2025-09-09
%global commit a5fbde82fd5ac017c9ef3c1a0bfdab46fe338d4c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global plugin_dir %(%___build_pre; pkg-config --variable=plugin_dir audacious)

%global aud_plugin_api %(grep '[ ]*#define[ ]*_AUD_PLUGIN_VERSION[ ]\\+' %{_includedir}/libaudcore/plugin.h 2>/dev/null | sed 's!.*_AUD_PLUGIN_VERSION[ ]*\\([0-9]\\+\\).*!\\1!')
%if 0%{aud_plugin_api} > 0
%global aud_plugin_dep Requires: audacious(plugin-api)%{?_isa} = %{aud_plugin_api}
%endif

Name: xmp-plugin-audacious
Version: 4.0.0.3.8
Release: 0.7.20250909git%{shortcommit}%{?dist}
Summary: Multi-format module playback plugin for Audacious using libxmp
Source: https://github.com/mschwendt/xmp-plugin-audacious/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
License: GPL-2.0-or-later
URL: http://xmp.sourceforge.net/
BuildRequires: make
BuildRequires: libtool automake autoconf gcc-c++
BuildRequires: audacious-devel >= 3.8
BuildRequires: libxmp-devel

%description
.

%package -n audacious-plugins-xmp
Summary: Multi-format module playback plugin for Audacious using libxmp
%if 0%{?fedora}
%{?aud_plugin_dep}
%else
Requires: audacious
%endif

%description -n audacious-plugins-xmp
Audacious input plugin based on Extended Module Player (xmp) library.

Libxmp is a library that renders module files to PCM data. It supports
over 90 mainstream and obscure module formats including Protracker (MOD),
Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse Tracker (IT).

Many compressed module formats are supported, including popular Unix, DOS,
and Amiga file packers including gzip, bzip2, SQSH, PowerPacker, etc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?fedora}
# Enforce availability of the audacious(plugin-api) dependency.
%{!?aud_plugin_dep:echo 'No audacious(plugin-api) dependency!' && exit -1}
%endif

# just a guard
pkg-config --print-variables audacious | grep ^plugin_dir

%autosetup -n %{name}-%{commit} -p1
autoreconf -i

%build
%configure
make OPTFLAGS="%{optflags}" V=1 %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files -n audacious-plugins-xmp
%license COPYING
%{plugin_dir}/Input/*.so
#exclude %%{plugin_dir}/Input/*.la

%changelog
%autochangelog
