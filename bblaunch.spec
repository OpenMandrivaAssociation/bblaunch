%define name bblaunch
%define version 0.0.3
%define release  10

Summary: An application launcher for Blackbox type window managers
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://folk.uio.no/~steingrd/%{name}-%{version}.tar.bz2
Source1: %{name}.1
Patch0: bblaunch-0.0.3.typo.patch
License: GPL
Group: Graphical desktop/Other
Url: http://blackboxwm.sourceforge.net/
BuildRequires: pkgconfig(x11)

%description
bblaunch is an application launcher that lets you set certain blackbox related
attributes on the launched program.  You can use it to run an application with
no decorations, to immediately have it sent to a specific workspace, to have it
visible on all workspaces and so on and so on.

%prep
%setup -q
%patch0 -p1 -b .typo

%build
# (blino) the default -O2 optimization makes bblaunch segfault
export CFLAGS="%optflags -O0"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
install -d -m 755 ${RPM_BUILD_ROOT}%{_mandir}/man1/
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 0.0.3-8mdv2011.0
+ Revision: 635005
- rebuild
- tighten BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.3-7mdv2011.0
+ Revision: 616742
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.0.3-6mdv2010.0
+ Revision: 424022
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.0.3-5mdv2009.0
+ Revision: 240442
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 15 2007 Pascal Terjan <pterjan@mandriva.org> 0.0.3-3mdv2008.0
+ Revision: 63758
- Import bblaunch



* Fri Dec 23 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.0.3-3mdk
- Fix BuildRequires
- use mkrel

* Fri Oct 21 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.0.3-2mdk
- Fix BuildRequires

* Sat Apr  2 2005 Olivier Blin <oblin@mandrakesoft.com> 0.0.3-1mdk
- initial Mandrakelinux release (Patch0 and man page from Debian)
