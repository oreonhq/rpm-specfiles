%global source0_hash 19a51ad759a547c35535f8bbbafd982aab647ebfb15b438d233e4102fd8761a3
%global realname lfe
Name:		erlang-%{realname}
Version:	2.2.2
Release:        1%{?dist}
Summary:        Lisp Flavoured Erlang
License:	Apache-2.0
URL:		https://github.com/lfe/%{realname}
VCS:		git:%{url}.git
Source0:        https://github.com/%{realname}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-lfe-0001-Restore-functions-removed-in-pre-R17-Erlang.patch
Patch:		erlang-lfe-0002-We-don-t-have-proper-yet.patch
Obsoletes:	emacs-erlang-lfe
Obsoletes:	emacs-erlang-lfe-el
Requires:	emacs-filesystem
# oreon:deps
BuildRequires:  emacs
BuildRequires:  erlang-proper
BuildRequires:  erlang-rebar3
BuildRequires:  gcc
# /oreon:deps
%description
Lisp Flavoured Erlang, is a lisp syntax front-end to the Erlang
compiler. Code produced with it is compatible with "normal" Erlang
code. An LFE evaluator and shell is also included.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{realname}-%{version}

%build

%{erlang3_compile}
gcc c_src/lfeexec.c $CFLAGS -fPIC -c -o c_src/lfeexec.o
gcc c_src/lfeexec.o $LDFLAGS -o bin/lfeexec
emacs -L emacs/ -batch -f batch-byte-compile emacs/inferior-lfe.el emacs/lfe-mode.el emacs/lfe-indent.el
%install
%{erlang3_install}
install -m 0755 -d %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/bin
install -p -m 0755 -D bin/*  %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/bin/
install -m 0755 -d %{buildroot}/%{_bindir}
ln -s %{_libdir}/erlang/lib/%{realname}-%{version}/bin/{lfe,lfe-test,lfec,lfedoc,lfeexec,lfescript} %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_emacs_sitelispdir}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 0644 emacs/inferior-lfe.el %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/inferior-lfe.elc %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-mode.el %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-mode.elc %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-indent.el %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-indent.elc %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-start.el %{buildroot}%{_emacs_sitestartdir}
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
