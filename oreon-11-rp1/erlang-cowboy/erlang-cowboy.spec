%global source0_hash 15a6bf9cac0c9e5ad658cd0d076fcfe5d15d916de87a9fadaae5112e870a1825
%global realname cowboy
Name:		erlang-%{realname}
Version:	2.19.0
Release:        1%{?dist}
BuildArch:	noarch
Summary:        Small, fast, modular HTTP server written in Erlang
License:	ISC
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/ninenines/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  dblatex
BuildRequires:  erlang-cowlib
BuildRequires:  erlang-ct_helper
BuildRequires:  erlang-gun
BuildRequires:  erlang-ranch
BuildRequires:  erlang-rebar3
BuildRequires:  libxml2
BuildRequires:  texlive-upquote
# /oreon:deps
%description
%{summary}.

%package doc
Summary: Documentation for %{name}
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{realname}-%{version}

%build

%{erlang3_compile}
a2x -v -f pdf CONTRIBUTING.asciidoc
a2x -v -f pdf doc/src/guide/book.asciidoc && mv doc/src/guide/book.pdf doc/guide.pdf
a2x -v -f chunked doc/src/guide/book.asciidoc && mv doc/src/guide/book.chunked/ doc/html/
%install
%{erlang3_install}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n erlang-cowboy-doc -f %{oreon_filedir}/erlang-cowboy-doc.list

%changelog

%autochangelog
