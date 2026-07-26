%global source0_hash 176615ff2fcfda6ce2a5bc6a2eeaf57a7fbb5810f87ab1bbe5ec63037caef47a

%global pkg epc

Name:           emacs-%{pkg}
Version:        0.1.1
Release:        15%{?dist}
Summary:        A RPC stack for Emacs Lisp

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/kiwanami/%{name}/
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fix make-network-process to work with Emacs >= 26
Patch0:         %{name}-0.1.1-asyncness.patch

BuildRequires:  emacs
BuildRequires:  emacs-ctable
BuildRequires:  emacs-deferred
Requires:       emacs(bin) >= %{_emacs_version}
Requires:       emacs-ctable
Requires:       emacs-deferred
BuildArch:      noarch

%description
This program is an asynchronous RPC stack for Emacs. Using this RPC stack, the
Emacs can communicate with the peer process smoothly. Because the protocol
employs S-expression encoding and consists of asynchronous communications, the
RPC response is fairly good.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{_emacs_bytecompile} %{pkg}.el %{pkg}s.el

%install
install -dm 0755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/
install -pm 0644 %{pkg}.el* %{pkg}s.el* -t $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/

%check
emacs --batch -q --no-site-file --no-splash \
    -L $RPM_BUILD_ROOT%{_emacs_sitelispdir}/%{pkg}/ \
    -l test-%{pkg}.el \
    -f cc:test-all

%files
%doc readme.md
%{_emacs_sitelispdir}/%{pkg}/

%changelog
%autochangelog
