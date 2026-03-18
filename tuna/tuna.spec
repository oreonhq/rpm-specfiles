%bcond oscilloscope %{undefined rhel}

Name: tuna
Version: 0.20
Release: 3%{?dist}
License: GPL-2.0-only AND LGPL-2.1-only
Summary: Application tuning GUI & command line utility
Source: https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.xz
URL: https://rt.wiki.kernel.org/index.php/Tuna
BuildArch: noarch
BuildRequires: python3-devel, gettext
Requires: python3-linux-procfs >= 0.6
# This really should be a Suggests...
# Requires: python-inet_diag

# Patches

%description
Provides interface for changing scheduler and IRQ tunables, at whole CPU and at
per thread/IRQ level. Allows isolating CPUs for use by a specific application
and moving threads and interrupts to a CPU by just dragging and dropping them.
Operations can be done on CPU sockets, understanding CPU topology.

Can be used as a command line utility without requiring the GUI libraries to be
installed.

%if %{with oscilloscope}
%package -n oscilloscope
Summary: Generic graphical signal plotting tool
Requires: python3-matplotlib-gtk3
Requires: python3-numpy
Requires: python3-cairocffi
Requires: gobject-introspection
Requires: tuna = %{version}-%{release}

%description -n oscilloscope
Plots stream of values read from standard input on the screen together with
statistics and a histogram.

Allows to instantly see how a signal generator, such as cyclictest, signaltest
or even ping, reacts when, for instance, its scheduling policy or real time
priority is changed, be it using tuna or plain chrt & taskset.
%endif

%prep
%autosetup -v -p1
# Delete setup.py so pyproject.toml build doesn't use it
rm -f setup.py
# Prepare tuna script for installation (save to a separate location to avoid directory conflict)
cp -p tuna-cmd.py %{_builddir}/tuna-script
# Compress man page
gzip -c docs/tuna.8 > %{_builddir}/tuna.8.gz

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tuna
# Install the tuna script
install -D -m 0755 %{_builddir}/tuna-script %{buildroot}%{_bindir}/tuna
# Install the compressed man page
install -D -m 0644 %{_builddir}/tuna.8.gz %{buildroot}%{_mandir}/man8/tuna.8.gz

mkdir -p %{buildroot}/%{_sysconfdir}/tuna/
mkdir -p %{buildroot}/%{_datadir}/tuna/help/kthreads
mkdir -p %{buildroot}/%{_datadir}/polkit-1/actions/
install -p -m644 tuna/tuna_gui.glade %{buildroot}/%{_datadir}/tuna/
install -p -m644 help/kthreads/* %{buildroot}/%{_datadir}/tuna/help/kthreads/
install -p -m644 etc/tuna/example.conf %{buildroot}/%{_sysconfdir}/tuna/
install -p -m644 etc/tuna.conf %{buildroot}/%{_sysconfdir}/
install -p -m644 org.tuna.policy %{buildroot}/%{_datadir}/polkit-1/actions/

%if %{without oscilloscope}
rm %{buildroot}%{_bindir}/oscilloscope
%endif

# l10n-ed message catalogues
for lng in `cat po/LINGUAS`; do
        po=po/"$lng.po"
        mkdir -p %{buildroot}/%{_datadir}/locale/${lng}/LC_MESSAGES
        msgfmt $po -o %{buildroot}/%{_datadir}/locale/${lng}/LC_MESSAGES/%{name}.mo
done

%find_lang %name

%files -f %{name}.lang -f %{pyproject_files}
%doc ChangeLog
%{_bindir}/tuna
%{_datadir}/tuna/
%{_mandir}/man8/tuna.8.gz
%{_sysconfdir}/tuna.conf
%{_sysconfdir}/tuna/*
%{_datadir}/polkit-1/actions/org.tuna.policy

%if %{with oscilloscope}
%files -n oscilloscope
%{_bindir}/oscilloscope
%doc docs/oscilloscope+tuna.html
%doc docs/oscilloscope+tuna.pdf
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.20-3
- Prepare for Oreon 11 (RP1)
