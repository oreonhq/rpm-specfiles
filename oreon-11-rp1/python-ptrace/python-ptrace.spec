%global source0_hash 56bbfef44eaf3a77be48138cca5767cdf471e8278fe1499f9b72f151907f25cf

Summary:       Debugger using ptrace written in Python
Name:          python-ptrace
Version:       0.9.9
Release:       11%{?dist}
License:       GPL-2.0-only
URL:           https://github.com/vstinner/python-ptrace
Source0:       https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: python3-devel
# See ptrace/syscall/names.py
ExcludeArch:   s390x
%global _description \
python-ptrace is a debugger using ptrace written in Python. \
Features: \
 o High level Python object API : PtraceDebugger and PtraceProcess \
 o Able to control multiple processes: catch fork events on Linux \
 o Read/write bytes to arbitrary address: take care of memory alignment \
   and split bytes to cpu word \
 o Execution step by step using ptrace_singlestep() \
   or hardware interruption 3 \
 o Dump registers, memory mappings, stack, etc. \
 o Syscall tracer and parser (strace.py command) \
 o Can use distorm disassembler (if available)

%description %_description
%package    -n python3-ptrace
Summary:       Debugger using ptrace written in Python 3
%description -n python3-ptrace %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
chmod 0644 examples/*.py
# requires https://github.com/gdabah/distorm
rm ptrace/pydistorm.py

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}
%{__python3} setup_cptrace.py build

%install

%{pyproject_install}
%pyproject_save_files -l ptrace
%{__python3} setup_cptrace.py install -O1 --skip-build --root %{buildroot}
rm -f %{buildroot}%{_bindir}/{gdb,strace}.{pyo,pyc}

%check
%pyproject_check_import
%{__python3} runtests.py || :

%files -n python3-ptrace -f %{pyproject_files}
%doc README.rst
%doc doc/* examples
%{_bindir}/gdb.py
%{_bindir}/strace.py
%{python3_sitearch}/cptrace.cpython-*.so
%{python3_sitearch}/cptrace-*-py*.egg-info

%changelog
%autochangelog
