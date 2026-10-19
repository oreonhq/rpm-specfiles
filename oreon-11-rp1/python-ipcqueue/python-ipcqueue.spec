%global source0_hash 92d3361afe04a24d89b0b25485f6634c8c51aad465ae7a564cc4b81f7e04cf64
Name:           python-ipcqueue
Version:        0.9.7
Release:        1%{?dist}
Summary:        POSIX and SYS V message queues to exchange data among processes
License:        BSD-3-Clause
URL:            https://pypi.org/project/ipcqueue/
Source0:        https://files.pythonhosted.org/packages/source/i/ipcqueue/ipcqueue-%{version}.tar.gz
Patch:          https://github.com/seifert/ipcqueue/pull/10.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ipcqueue = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-ipcqueue
Summary:        POSIX and SYS V message queues to exchange data among processes
%description -n python3-ipcqueue

%package doc
Summary:       HTML documention for python3-ipcqueue
BuildArch:     noarch
%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ipcqueue-%{version}
%oreon_prep
%build

%pyproject_wheel
make -C doc html man
rm doc/_build/html/.buildinfo
%install
%pyproject_install
install -D -m 0644 doc/_build/man/ipcqueue.1 %{buildroot}%{_mandir}/man3/ipcqueue.3
%oreon_autofiles python3-ipcqueue usr/lib/python3*/site-packages/ipcqueue* usr/lib64/python3*/site-packages/ipcqueue* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ipcqueue* usr/lib64/python3*/site-packages/ipcqueue* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files
%files -n python3-ipcqueue -f %{oreon_filedir}/python3-ipcqueue.list
%files -n python-ipcqueue-doc -f %{oreon_filedir}/python-ipcqueue-doc.list

%changelog

%autochangelog
