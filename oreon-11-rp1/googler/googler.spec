%global source0_hash bd59af407e9a45c8a6fcbeb720790cb9eccff21dc7e184716a60e29f14c68d54

Name:       googler
Version:    4.3.2
Release:    13%{?dist}
Summary:    Access google search, google site search, google news from the terminal

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:    GPL-3.0-or-later
URL:        https://github.com/jarun/googler
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make

%description
googler is a power tool to access Google (Web & News) websites and Google Site
Search website from the command-line. It shows the title, URL and abstract
for each result, which can be directly opened in a browser from the terminal.
Results are fetched in pages (with page navigation). Supports sequential
searches in a single googler instance.

googler was initially written to cater to headless servers without X. You can
integrate it with a text-based browser. However, it has grown into a very handy
and flexible utility that delivers much more. For example, fetch any number of
results or start anywhere, limit search by any duration, define aliases to
google search any number of websites, switch domains easily... all of this
in a very clean interface without ads or stray URLs. The shell completion
scripts make sure you don't need to remember any options.

googler isn't affiliated to Google in any way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
sed -i '1s/env //' googler

%build
make disable-self-upgrade

%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/googler-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  auto-completion/fish/googler.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_googler

%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bash-completion/completions/googler-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/googler.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_googler

%changelog
%autochangelog
