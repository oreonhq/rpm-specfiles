%global source0_hash 9302ad27c4895e696b73cb9d9ccdaf5a00e180caa97b88e5d1d529b4113cfa64

%global forgeurl https://github.com/jarikomppa/emu8051
%global gitcommit 5dc681275151c4a5d7b85ec9ff4ceb1b25abd5a8
%global gitdate 20220911
%global gitshort %(echo %{gitcommit} | cut -c 1-8)

Name:           emu8051
Version:        0~%{gitdate}git%{gitshort}
Release:        %autorelease
Summary:        8051/8052 emulator with curses-based UI

License:        MIT
URL:            https://solhsa.com/8051.html
VCS:            git:%{forgeurl}
Source0:        %{forgeurl}/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
This is a simulator of the 8051/8052 microcontrollers. For sake of simplicity,
I'm only referring to 8051, although the emulator can emulate either one. For
more information about the 8-bit chip(s), please check out 8052mcu.com or
look up the data sheets. Intel, being the originator of the architecture,
naturally has information as well.

The 8051 is a pretty easy chip to play with, in both hardware and software.
Hence, it's a good chip to use as an example when teaching about computer
hardware. Unfortunately, the simulators in use in my school were a bit outdated,
so I decided to write a new one.

The scope of the emulator is to help test and debug 8051 assembler programs.
What is particularily left out is clock-cycle exact simulation of processor pins.
(For instance, MUL is a 48-clock operation on the 8051. On which clock cycle does
the CPU read the operands? Or write the result?). Such simulation might help in
designing some hardware, but for most uses it is unneccessary and complicated.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gitcommit}

%build
%make_build BIN=%{name}

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -p %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
