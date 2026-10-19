%global source1_hash 8f6cc7ec5d0ba5b4bbb6bfc6fe8d013ecf250fc330bdd4f4d2e6dd57e6632f0f
%global source0_hash 2f87be1702583ecbeee82c0ad4d6353de96463cfa0fa6e7557e05f68d90da869
%global upstream elixir-lang
%global debug_package %{nil}
Name:     elixir
Version:  1.20.4
%global __requires_exclude_from ^%{_datadir}/%{name}/%{version}/bin/.+\\.ps1$
Release:        1%{?dist}
Summary:        A modern approach to programming for the Erlang VM
License:  Apache-2.0
URL:      https://elixir-lang.org/
VCS:      git:https://github.com/%{upstream}/%{name}.git
Source0:        https://github.com/%{upstream}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:  https://github.com/%{upstream}/%{name}/releases/download/v%{version}/Docs.zip#/%{name}-%{version}-doc.zip
Patch:    elixir-0001-Fix-shebang.patch
Patch:    increase-timeouts-for-tests.patch
%ifnarch riscv64 %{ix86}
%endif
%ifarch %{java_arches}
Recommends: erlang-doc
%endif
# oreon:deps
BuildRequires:  erlang-compiler
BuildRequires:  erlang-crypto
BuildRequires:  erlang-dialyzer
BuildRequires:  erlang-doc
BuildRequires:  erlang-erts
BuildRequires:  erlang-eunit
BuildRequires:  erlang-inets
BuildRequires:  erlang-kernel
BuildRequires:  erlang-parsetools
BuildRequires:  erlang-public_key
BuildRequires:  erlang-rebar3
BuildRequires:  erlang-sasl
BuildRequires:  erlang-stdlib
BuildRequires:  erlang-tools
BuildRequires:  erlang-xmerl
BuildRequires:  git
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
Elixir is a programming language built on top of the Erlang VM.
As Erlang, it is a functional language built to support distributed,
fault-tolerant, non-stop applications with hot code swapping.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Unpack the HTML documentation (Source1)
%setup -q -T -c -n %{name}-%{version}/docs -a 1
find -name ".build" -exec rm \{\} \;

# Unpack elixir itself (Source0)
%autosetup -p1 -D

# Remove windows-specific scripts
find -name '*.bat' -exec rm \{\} \;

# Let the Makefile speak!
sed -i '/^Q\s*:=/d' Makefile

%build

export REBAR3=/usr/bin/rebar3
export ERL_LIBS=/usr/share/erlang/lib/
make compile
make build_man
%check

rm -f ./lib/mix/test/fixtures/rebar3
export REBAR3=/usr/bin/rebar3
export ERL_LIBS=/usr/share/erlang/lib/
make test
%install
mkdir -p %{buildroot}/%{_datadir}/%{name}/%{version}
cp -ra bin lib %{buildroot}/%{_datadir}/%{name}/%{version}
mkdir -p %{buildroot}/%{_bindir}
ln -s %{_datadir}/%{name}/%{version}/bin/{elixir,elixirc,iex,mix} %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a man/elixir.1 man/elixirc.1 man/iex.1 man/mix.1 %{buildroot}/%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package doc
Summary: Documentation for the elixir language and tools
%description doc
HTML documentation for eex, elixir, iex, logger and mix.

%files -f %{oreon_filedir}/main.list
%files -n elixir-doc -f %{oreon_filedir}/elixir-doc.list

%changelog

%autochangelog
