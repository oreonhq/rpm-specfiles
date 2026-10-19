%global source0_hash 21d670851df8a726a9a8e620ec4557c3fd9cc490a06a57ddddfc5a9bdc8f9df0
%global maketrace .SHELLFLAGS=-xc
Name:		oidc-agent
Version:	5.3.4
Release:        2%{?dist}
Summary:        Managing OpenID Connect tokens on the command line
License:	MIT AND ISC AND LGPL-2.1-or-later AND BSD-2-Clause
URL:		https://github.com/indigo-dc/%{name}
Source0:        https://github.com/indigo-dc/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:	%{ix86}
Patch0:		0001-Fix-different-return-type-in-.h-and-.c-file.patch
Patch1:		0002-Fix-warnings-about-wrong-argument-types-when-calling.patch
%global webkitgtk webkit2gtk-4.0
# oreon:deps
BuildRequires:  cjson-devel
BuildRequires:  clibs-list-devel
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  help2man
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libsodium-devel
BuildRequires:  make
BuildRequires:  qrencode-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  webkitgtk4-devel
# /oreon:deps
%description
oidc-agent is a set of tools to manage OpenID Connect tokens and make
them easily usable from the command line. We followed the ssh-agent
design, so users can handle OIDC tokens in a similar way as they do
with ssh keys.

oidc-agent is usually started in the beginning of an X-session or a
login session. Through use of environment variables the agent can be
located and used to handle OIDC tokens.

The agent initially does not have any account configurations
loaded. You can load an account configuration by using
oidc-add. Multiple account configurations may be loaded in oidc-agent
concurrently. oidc-add is also used to remove a loaded configuration
from oidc-agent. oidc-gen is used to initially generate an account
configurations file.

%package cli
Summary:	Command line tool for obtaining OpenID Connect tokens
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description cli
oidc-agent is a set of tools to manage OpenID Connect tokens and make
them easily usable from the command line. These tools follow ssh-agent
design, so OIDC tokens can be handled in a similar way as ssh keys.
The agent stores multiple configurations and their associated refresh
tokens securely.

This tool consists of five programs:
  - oidc-agent that handles communication with the OIDC provider
  - oidc-gen that generates config files
  - oidc-add that loads (and unloads) configuration into the agent
  - oidc-token that can be used to get access token on the command line
  - oidc-key-chain that re-uses oidc-agent across logins

%package desktop
Summary:	GUI integration for obtaining OpenID Connect tokens
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-cli = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < %{version}-%{release}
%description desktop
Desktop integration files for oidc-gen and oidc-agent.

This package adds two ways for supporting the usage of oidc-agent in a
graphical environment:
 - The .desktop file to leverage browser integration to support the
   authorization code flow in oidc-gen.
 - The Xsession file to consistently set the environment variables
   necessary to for client tools to connect to the oidc-agent daemon.

%package libs
Summary:	Library for oidc-agent
%description libs
oidc-agent is a command line tool for obtaining OpenID Connect tokens
on the command line.

This package provides a library for easy communication with oidc-agent.
Applications can use this library to request access tokens from
oidc-agent.

%package devel
Summary:	Headers for the oidc-agent library
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description devel
oidc-agent is a command line tool for obtaining OpenID Connect tokens
on the command line.

This package provides headers for the oidc-agent library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

# Remove bundled cJSON and clib-list (use system versions)
rm -rf lib/cJSON lib/list

%build

%set_build_flags
%make_build %{maketrace} WEBKITGTK=%{webkitgtk}
%install
%set_build_flags
%make_install install_includes %{maketrace} \
	WEBKITGTK=%{webkitgtk} \
	PREFIX=%{buildroot} \
	INCLUDE_PATH=%{buildroot}%{_includedir} \
	LIB_PATH=%{buildroot}%{_libdir} \
	BIN_AFTER_INST_PATH=%{_prefix} \
	CONFIG_AFTER_INST_PATH=%{_sysconfdir}
ln -s liboidc-agent.so.%{version} %{buildroot}%{_libdir}/liboidc-agent.so
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post cli

%tmpfiles_create %{name}.conf
%files -f %{oreon_filedir}/main.list
%files -n oidc-agent-cli -f %{oreon_filedir}/oidc-agent-cli.list
%files -n oidc-agent-desktop -f %{oreon_filedir}/oidc-agent-desktop.list
%files -n oidc-agent-libs -f %{oreon_filedir}/oidc-agent-libs.list
%files -n oidc-agent-devel -f %{oreon_filedir}/oidc-agent-devel.list

%changelog

%autochangelog
