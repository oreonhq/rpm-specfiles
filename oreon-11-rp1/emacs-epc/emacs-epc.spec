%global source0_hash 176615ff2fcfda6ce2a5bc6a2eeaf57a7fbb5810f87ab1bbe5ec63037caef47a
%global pkg epc
Name:           emacs-%{pkg}
Version:        0.1.1
Release:        1%{?dist}
Summary:        A RPC stack for Emacs Lisp
License:        GPL-3.0-or-later
URL:            https://github.com/kiwanami/%{name}/
Source0:        https://github.com/kiwanami/%{name}//archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-0.1.1-asyncness.patch
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-ctable
Requires:       emacs-deferred
BuildArch:      noarch
# oreon:deps
BuildRequires:  emacs
BuildRequires:  emacs-ctable
BuildRequires:  emacs-deferred
# /oreon:deps
%description
This program is an asynchronous RPC stack for Emacs. Using this RPC stack, the
Emacs can communicate with the peer process smoothly. Because the protocol
employs S-expression encoding and consists of asynchronous communications, the
RPC response is fairly good.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{_emacs_bytecompile} %{pkg}.el %{pkg}s.el
%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* %{pkg}s.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
%oreon_autofiles main

%check

emacs --batch -q --no-site-file --no-splash \
    -L $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/ \
    -l test-%{pkg}.el \
    -f cc:test-all
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
