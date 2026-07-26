%global source0_hash 1e23686b8887ebe461786c059d848b412188c635929071955d134041b07996a7

Name:           netsed
Version:        1.4
Release:        3%{?dist}
Summary:        Tool to modify network packets

License:        GPL-2.0-or-later
URL:            http://silicone.homelinux.org/projects/netsed/
Source0:        http://silicone.homelinux.org/release/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  doxygen
BuildRequires:  graphviz

%description
NetSED is small and handful utility designed to alter the contents of
packets forwarded through your network in real time. It is really useful
for network hackers in following applications:

* black-box protocol auditing - whenever there are two or more
  proprietary boxes communicating over undocumented protocol (by enforcing 
  changes in ongoing transmissions, you will be able to test if tested 
  application is secure),
* fuzz-alike experiments, integrity tests - whenever you want to test 
  stability of the application and see how it ensures data integrity,
* other common applications - fooling other people, content filtering,
  etc - choose whatever you want to.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"
make doc

%install
install -Dp -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc LICENSE NEWS README TODO html/
%{_bindir}/%{name}

%changelog
%autochangelog
