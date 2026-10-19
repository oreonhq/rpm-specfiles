%global source0_hash none
Name:           emacs-filesystem
Epoch:          1
Version:        30.2
Release:        1%{?dist}
Summary:        Emacs filesystem layout
URL:            https://www.gnu.org/software/emacs/
License:        CC0-1.0
# oreon:deps

# /oreon:deps
%description
This package provides some directories which are required by other
packages that add functionality to Emacs.

%install
install -m 0755 -d %{buildroot}%{_datadir}/emacs \
                   %{buildroot}%{_datadir}/emacs/site-lisp \
                   %{buildroot}%{_datadir}/emacs/site-lisp/site-start.d \
                   %{buildroot}%{_libdir}/emacs/site-lisp
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Sat May 16 2026 Oreon Packaging Team <packaging@oreonhq.com> - 30.2-1
- Import
