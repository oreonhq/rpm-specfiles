%global source0_hash c15bc10712835d3a9bcda780dc9453362567bf48d1185905dc7ef2334d79aadd

%global compdir %(pkg-config --variable=completionsdir bash-completion)
%global __requires_exclude .*Acme::Cow.*

%global cowsdir %{_datadir}/%{name}/cows
%global sitecowsdir %{_datadir}/%{name}/site-cows

Name:           cowsay
Version:        3.8.4
Release:        5%{?dist}
Summary:        Configurable speaking/thinking cow
License:        GPL-2.0-or-later
URL:            https://github.com/cowsay-org/cowsay
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        cowsay.bashcomp
Source2:        animalsay

BuildArch:      noarch
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  perl-generators
Requires:       perl-Encode
# introduced /usr/share/bash-completion/...
Requires:       filesystem >= 3.6-1

%description
cowsay is a configurable talking cow, written in Perl.  It operates
much as the figlet program does, and it is written in the same spirit
of silliness.
It generates ASCII pictures of a cow with a message. It can also generate
pictures of other animals.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
echo No need to build anything

%install
# At least for cowsay-3.7.0, replace upstream's "make install" by our
# own installation code.
install -d -m 0755         $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/%{name} $RPM_BUILD_ROOT%{_bindir}
ln -s              %{name} $RPM_BUILD_ROOT%{_bindir}/cowthink

install -d -m 0755           $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 0644 man/man1/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
ln -s              %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/cowthink.1

install -d -m 0755              $RPM_BUILD_ROOT%{cowsdir}
install -p -m 0644 share/cowsay/cows/* $RPM_BUILD_ROOT%{cowsdir}

install -d -m 0755              $RPM_BUILD_ROOT%{sitecowsdir}

install -d -m 0755              $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/cowpath.d

# Install actions specific to the Fedora package

# License issue
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/cows/daemon.cow
# animalsay
install -p -m 0755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
# bash completion file
install -d -m 0755            $RPM_BUILD_ROOT%{compdir}
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{compdir}/%{name}

%files
%doc CHANGELOG.md LICENSE.txt README README.md
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/cowpath.d
%{_bindir}/animalsay
%{_bindir}/cowsay
%{_bindir}/cowthink
%{_mandir}/man1/cowsay.1*
%{_mandir}/man1/cowthink.1*
%dir %{_datadir}/%{name}
%{cowsdir}
%exclude %{cowsdir}/bong.cow
%exclude %{cowsdir}/head-in.cow
%exclude %{cowsdir}/mutilated.cow
%dir %{sitecowsdir}
%{compdir}/%{name}

%changelog
%autochangelog
